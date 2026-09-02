#!/usr/bin/env bash
# Smoke test for scripts/add_bg_bgm.sh
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

ffmpeg -y -hide_banner -loglevel error \
  -f lavfi -i "color=c=black:s=320x180:d=1,format=yuv420p" \
  -f lavfi -i "color=c=white:s=80x40:d=1" \
  -filter_complex "[0:v][1:v]overlay=120:70" -t 1 "$TMP/in.mp4"
ffmpeg -y -hide_banner -loglevel error -f lavfi -i "color=c=0x336699:s=400x300:d=1" -frames:v 1 "$TMP/bg.png"
ffmpeg -y -hide_banner -loglevel error -f lavfi -i "sine=frequency=440:duration=2" "$TMP/bgm.wav"

"$ROOT/scripts/add_bg_bgm.sh" \
  --input "$TMP/in.mp4" --bg "$TMP/bg.png" --bgm "$TMP/bgm.wav" \
  --output "$TMP/out.mp4" --fade 0.2 >/dev/null

types="$(ffprobe -v error -show_entries stream=codec_type -of csv=p=0 "$TMP/out.mp4" | tr '\n' ' ')"
echo "$types" | grep -q video || { echo "missing video"; exit 1; }
echo "$types" | grep -q audio || { echo "missing audio"; exit 1; }
echo "ok: $types"
