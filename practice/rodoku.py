# 文字列のリストを受け取って、その朗読の音声とメタデータのリストをVoiceVoxのAPIで生成し、各音声の長さに基づいて、画面内の文章を更新する動画も生成する

import requests
import json
import os
import time

def generate_voice_from_texts(
        text_list:list[str],
        output_dir:str = "/Volumes/T7/VOICEVOX/",
        sub_dir_name:str = "voice_outputs",
        speaker_id:int = 3
)-> list[dict]:
    voice_info_list = []
    base_url = "http://127.0.0.1:50021"

    os.makedirs(output_dir,exist_ok=True)

    for i,text in enumerate(text_list):
        output_filename = os.path.join(output_dir, f"output_{i}.wav")
        try:
            print
        except Exception as e:
            print(e)



    return voice_info_list

def generate_voice_from_text_list(
    text_list: list[str],
    output_dir: str = "/Volumes/T7/VOICEVOX/voice_outputs",
    speaker_id: int = 3 # デフォルトのずんだもん
) -> list[dict]:
    voice_info_list = []
    base_url = "http://127.0.0.1:50021"

    # 出力ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)

    for i, text in enumerate(text_list):
        output_filename = os.path.join(output_dir, f"output_{i}.wav")

        try:
            # 1. 音声合成クエリを作成
            # (query_creation_optionsは必要に応じて調整)
            query_params = {
                "text": text,
                "speaker": speaker_id,
            }
            response = requests.post(
                f"{base_url}/audio_query",
                params=query_params
            )
            response.raise_for_status()  # HTTPエラーがあれば例外を発生
            audio_query = response.json()

            # 2. 音声ファイルを生成
            synthesis_params = {
                "speaker": speaker_id,
            }
            headers = {"Content-Type": "application/json"}
            response = requests.post(
                f"{base_url}/synthesis",
                headers=headers,
                params=synthesis_params,
                data=json.dumps(audio_query)
            )
            response.raise_for_status()

            # 3. 生成された音声データを保存
            with open(output_filename, "wb") as f:
                f.write(response.content)

            # 4. 音声ファイルのデュレーションを取得 (簡易的な方法)
            # より正確なデュレーション取得には、別途ライブラリ (e.g., pydub, soundfile) が必要ですが、
            # 今回はAPIから取得できる情報がないため、簡易的な近似値としてクエリのフレームレートとフレーム数から計算します。
            # VoiceVox APIのaudio_queryの結果にdurationが直接含まれていないため、
            # ここでは音声ファイルの実際の再生時間ではなく、audio_queryの情報から計算します。
            # もし正確なデュレーションが必要な場合は、生成されたWAVファイルを読み込んで解析する必要があります。
            # ここでは、簡略化のため、audio_query の "outputSamplingRate" と "outputStereo" などの情報から
            # 後のステップで別途計算するか、別途ライブラリを使用して計算することにします。
            # ここでは便宜上、仮の値を入れます。実際にはファイルから読み取るべきです。
            # （VoiceVox API自体が生成時にデュレーションを返さないため、ファイルを読んで計算する必要がある）

            # 実際にWAVファイルのデュレーションを計算する（pydubが必要）
            try:
                from pydub import AudioSegment
                audio = AudioSegment.from_wav(output_filename)
                duration_seconds = audio.duration_seconds
            except ImportError:
                print("pydubがインストールされていません。音声ファイルのデュレーションは0として扱われます。")
                print("`pip install pydub` でインストールできます。")
                duration_seconds = 0.0
            except Exception as e:
                print(f"音声ファイルのデュレーション取得中にエラーが発生しました: {e}")
                duration_seconds = 0.0


            voice_info_list.append({
                "path": output_filename,
                "duration": duration_seconds
            })
            print(f"「{text[:20]}...」の音声を生成し、{output_filename}に保存しました。デュレーション: {duration_seconds:.2f}秒")

        except requests.exceptions.RequestException as e:
            print(f"VoiceVox APIとの通信中にエラーが発生しました: {e}")
            print(f"テキスト: {text}")
            continue
        except Exception as e:
            print(f"音声生成中に予期せぬエラーが発生しました: {e}")
            print(f"テキスト: {text}")
            continue

        # APIへの連続リクエストを避けるための短い遅延
        time.sleep(0.1)

    return voice_info_list

if __name__ == "__main__":
    # 使用例
    texts_to_synthesize = [
        "こんにちは。VoiceVoxのAPIテストです。",
        "これは二つ目のテキストです。",
        "短い文章でも問題なく動作します。",
        "長文の場合は、生成に時間がかかることがありますのでご注意ください。",
        "今日はとても良い天気ですね。",
        "明日はきっと、もっと良い日になるでしょう！"
    ]

    # 必要に応じて話者IDを変更してください
    # VoiceVoxエディタの「話者」タブで確認できます
    # 例: ずんだもん: 3, 四国めたん: 2
    speaker_id_to_use = 3

    print(f"出力ディレクトリ: voice_outputs に音声を保存します。")
    print(f"使用話者ID: {speaker_id_to_use}")

    generated_voices_info = generate_voice_from_text_list(
        texts_to_synthesize,
        speaker_id=speaker_id_to_use
    )

    print("\n--- 生成された音声情報 ---")
    for info in generated_voices_info:
        print(f"パス: {info['path']}, デュレーション: {info['duration']:.2f}秒")

    print("\n全ての音声が正常に生成されたか確認してください。")
    print("VoiceVox APIサーバーが起動していることを確認してください。")