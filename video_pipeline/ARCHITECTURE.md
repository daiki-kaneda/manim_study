# 動画ビルド（クリーンアーキテクチャ）

```
CLI / composition
        ↓
BuildVideoUseCase
        ↓
  VideoRendererPort      PostProcessorPort      StoragePort      UploaderPort
        ↑                      ↑                    ↑                ↑
  ManimRenderer        FfmpegPostProcessor     LocalStorage    YouTubeUploader
```

ユースケースは「生成 →（任意）後処理 → ローカル保存 →（任意）アップロード」だけを知る。
Manim・ffmpeg・YouTube はアダプタの外に出さない。
