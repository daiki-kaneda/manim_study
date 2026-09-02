from __future__ import annotations

import shutil
from pathlib import Path

from video_pipeline.application.ports.storage import StoragePort
from video_pipeline.domain.errors import StorageError


class LocalStorage(StoragePort):
    def save(self, source: Path, dest_dir: Path, filename: str) -> Path:
        if not source.is_file():
            raise StorageError(f"保存元がありません: {source}")
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / filename
        try:
            if source.resolve() != dest.resolve():
                shutil.copy2(source, dest)
        except OSError as exc:
            raise StorageError(f"ローカル保存に失敗しました: {exc}") from exc
        return dest
