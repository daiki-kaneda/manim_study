#!/usr/bin/env bash
# Overlay a local background and/or loop BGM onto a Manim render.
# Paths can come from flags or from local/media.env (not committed).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ENV_FILE="${MANIM_MEDIA_ENV:-$ROOT/local/media.env}"

usage() {
  cat <<'EOF'
Usage:
  scripts/add_bg_bgm.sh --input <video> [options]

Add a local background image/video and/or BGM to a Manim MP4 for local preview.

Options:
  --input PATH       Manim output video (required)
  --bg PATH          Background image or video (optional)
  --bgm PATH         BGM audio file (optional)
  --output PATH      Output MP4 (default: <input>_muxed.mp4)
  --volume N         BGM gain, 0–1 (default: 0.18)
  --fade SEC         Fade in/out length in seconds (default: 2)
  --mode MODE        colorkey (default) | screen | opaque
  --colorkey HEX     Key color without # (default: 000000)
  --similarity N     Colorkey similarity 0–1 (default: 0.10)
  --dry-run          Print ffmpeg command and exit
  -h, --help         Show this help

At least one of --bg or --bgm is required (or MANIM_BG_PATH / MANIM_BGM_PATH).

Environment (optional file: local/media.env):
  MANIM_BG_PATH, MANIM_BGM_PATH, MANIM_BGM_VOLUME, MANIM_BGM_FADE
  MANIM_BG_MODE, MANIM_COLORKEY, MANIM_COLORKEY_SIMILARITY

Examples:
  scripts/add_bg_bgm.sh --input media/videos/.../TriangleArea.mp4 \\
      --bg ~/Movies/bg.png --bgm ~/Music/math.mp3

  # After copying local/media.env.example → local/media.env
  scripts/add_bg_bgm.sh --input media/videos/.../TriangleArea.mp4
EOF
}

die() {
  echo "error: $*" >&2
  exit 1
}

need_cmd() {
  command -v "$1" >/dev/null 2>&1 || die "$1 が見つかりません"
}

is_image() {
  local mime
  mime="$(file -b --mime-type "$1" 2>/dev/null || true)"
  case "$mime" in
    image/*) return 0 ;;
  esac
  case "${1##*.}" in
    png|jpg|jpeg|webp|bmp|tif|tiff) return 0 ;;
  esac
  return 1
}

ffprobe_val() {
  ffprobe -v error "$@"
}

duration_sec() {
  ffprobe_val -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$1"
}

has_audio() {
  local n
  n="$(ffprobe_val -select_streams a -show_entries stream=index -of csv=p=0 "$1" | wc -l | tr -d ' ')"
  [[ "${n:-0}" -gt 0 ]]
}

video_size() {
  ffprobe_val -select_streams v:0 -show_entries stream=width,height -of csv=p=0:s=x "$1"
}

# --- defaults ---
INPUT=""
BG="${MANIM_BG_PATH:-}"
BGM="${MANIM_BGM_PATH:-}"
OUTPUT="${MANIM_MUX_OUTPUT:-}"
VOLUME="${MANIM_BGM_VOLUME:-0.18}"
FADE="${MANIM_BGM_FADE:-2}"
MODE="${MANIM_BG_MODE:-colorkey}"
COLORKEY="${MANIM_COLORKEY:-000000}"
SIMILARITY="${MANIM_COLORKEY_SIMILARITY:-0.10}"
DRY_RUN=0

if [[ -f "$ENV_FILE" ]]; then
  # shellcheck disable=SC1090
  set -a
  source "$ENV_FILE"
  set +a
  BG="${BG:-${MANIM_BG_PATH:-}}"
  BGM="${BGM:-${MANIM_BGM_PATH:-}}"
  OUTPUT="${OUTPUT:-${MANIM_MUX_OUTPUT:-}}"
  VOLUME="${MANIM_BGM_VOLUME:-$VOLUME}"
  FADE="${MANIM_BGM_FADE:-$FADE}"
  MODE="${MANIM_BG_MODE:-$MODE}"
  COLORKEY="${MANIM_COLORKEY:-$COLORKEY}"
  SIMILARITY="${MANIM_COLORKEY_SIMILARITY:-$SIMILARITY}"
fi

while [[ $# -gt 0 ]]; do
  case "$1" in
    --input) INPUT="${2:-}"; shift 2 ;;
    --bg) BG="${2:-}"; shift 2 ;;
    --bgm) BGM="${2:-}"; shift 2 ;;
    --output) OUTPUT="${2:-}"; shift 2 ;;
    --volume) VOLUME="${2:-}"; shift 2 ;;
    --fade) FADE="${2:-}"; shift 2 ;;
    --mode) MODE="${2:-}"; shift 2 ;;
    --colorkey) COLORKEY="${2:-}"; shift 2 ;;
    --similarity) SIMILARITY="${2:-}"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) die "不明な引数: $1" ;;
  esac
done

need_cmd ffmpeg
need_cmd ffprobe

[[ -n "$INPUT" ]] || die "--input が必要です"
[[ -f "$INPUT" ]] || die "入力動画がありません: $INPUT"
[[ -n "$BG" || -n "$BGM" ]] || die "--bg か --bgm（または local/media.env）が必要です"

if [[ -n "$BG" ]]; then
  [[ -f "$BG" ]] || die "背景ファイルがありません: $BG"
fi
if [[ -n "$BGM" ]]; then
  [[ -f "$BGM" ]] || die "BGMファイルがありません: $BGM"
fi

case "$MODE" in
  colorkey|screen|opaque) ;;
  *) die "--mode は colorkey / screen / opaque のいずれかです" ;;
esac

if [[ -z "$OUTPUT" ]]; then
  OUTPUT="${INPUT%.*}_muxed.mp4"
fi

DUR="$(duration_sec "$INPUT")"
[[ -n "$DUR" && "$DUR" != "N/A" ]] || die "動画の長さを取得できません: $INPUT"
WH="$(video_size "$INPUT")"
WIDTH="${WH%x*}"
HEIGHT="${WH#*x}"
FADE="$(awk -v d="$DUR" -v f="$FADE" 'BEGIN { if (f < 0) f=0; if (d > 0 && f > d/2) f=d/2; printf "%.3f", f }')"
FADE_START="$(awk -v d="$DUR" -v f="$FADE" 'BEGIN { s=d-f; if (s<0) s=0; printf "%.3f", s }')"

mkdir -p "$(dirname "$OUTPUT")"

args=(ffmpeg -y -hide_banner)
filter=""
maps=()
v_in=0
a_sources=()

if [[ -n "$BG" ]]; then
  if is_image "$BG"; then
    args+=(-loop 1 -i "$BG")
  else
    args+=(-stream_loop -1 -i "$BG")
  fi
  args+=(-i "$INPUT")
  fg_idx=1
  bg_idx=0
  v_in=2
  bg_scale="[${bg_idx}:v]scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=increase,crop=${WIDTH}:${HEIGHT},setsar=1[bg]"
  fg_scale="[${fg_idx}:v]scale=${WIDTH}:${HEIGHT}:force_original_aspect_ratio=decrease,pad=${WIDTH}:${HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=black,setsar=1"
  case "$MODE" in
    colorkey)
      filter+="${bg_scale};${fg_scale},colorkey=0x${COLORKEY}:${SIMILARITY}:0.08,format=rgba[fg];"
      filter+="[bg][fg]overlay=0:0:shortest=1,format=yuv420p[vout]"
      ;;
    screen)
      filter+="${bg_scale};${fg_scale},format=gbrp[fg];"
      filter+="[bg][fg]blend=all_mode=screen:shortest=1,format=yuv420p[vout]"
      ;;
    opaque)
      filter+="${fg_scale}[vout]"
      ;;
  esac
  maps+=(-map "[vout]")
else
  args+=(-i "$INPUT")
  maps+=(-map 0:v:0)
  v_in=1
fi

if has_audio "$INPUT"; then
  a_sources+=("${fg_idx:-0}:a")
fi

if [[ -n "$BGM" ]]; then
  args+=(-stream_loop -1 -i "$BGM")
  bgm_idx="$v_in"
  a_sources+=("${bgm_idx}:a")
fi

if [[ ${#a_sources[@]} -eq 1 && -n "$BGM" ]]; then
  filter+="${filter:+;}[${a_sources[0]}]volume=${VOLUME},afade=t=in:st=0:d=${FADE},afade=t=out:st=${FADE_START}:d=${FADE}[aout]"
  maps+=(-map "[aout]")
elif [[ ${#a_sources[@]} -eq 1 ]]; then
  maps+=(-map "${a_sources[0]}")
elif [[ ${#a_sources[@]} -ge 2 ]]; then
  mix_in=""
  i=0
  for src in "${a_sources[@]}"; do
    if [[ "$src" == *":a" && -n "$BGM" && "$src" == "${bgm_idx}:a" ]]; then
      filter+="${filter:+;}[${src}]volume=${VOLUME}[bgm${i}]"
      mix_in+="[bgm${i}]"
    else
      filter+="${filter:+;}[${src}]aformat=sample_fmts=fltp:channel_layouts=stereo[src${i}]"
      mix_in+="[src${i}]"
    fi
    i=$((i + 1))
  done
  filter+=";${mix_in}amix=inputs=${#a_sources[@]}:duration=first:dropout_transition=0,afade=t=in:st=0:d=${FADE},afade=t=out:st=${FADE_START}:d=${FADE}[aout]"
  maps+=(-map "[aout]")
fi

if [[ -n "$filter" ]]; then
  args+=(-filter_complex "$filter")
fi
args+=("${maps[@]}" -t "$DUR" -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p)
if [[ ${#a_sources[@]} -gt 0 ]]; then
  args+=(-c:a aac -b:a 192k)
else
  args+=(-an)
fi
args+=(-movflags +faststart "$OUTPUT")

if [[ "$DRY_RUN" -eq 1 ]]; then
  printf '%q ' "${args[@]}"
  echo
  exit 0
fi

echo "input : $INPUT (${WIDTH}x${HEIGHT}, ${DUR}s)"
[[ -n "$BG" ]] && echo "bg    : $BG  mode=$MODE"
[[ -n "$BGM" ]] && echo "bgm   : $BGM  volume=$VOLUME fade=${FADE}s"
echo "output: $OUTPUT"

"${args[@]}"

echo "done: $OUTPUT"
