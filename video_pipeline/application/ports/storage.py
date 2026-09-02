from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path


class StoragePort(ABC):
    """Persist the finished video locally."""

    @abstractmethod
    def save(self, source: Path, dest_dir: Path, filename: str) -> Path:
        """Copy or move ``source`` into ``dest_dir/filename`` and return that path."""
