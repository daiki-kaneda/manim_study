from __future__ import annotations

import json
from pathlib import Path

from video_pipeline.application.ports.uploader import UploaderPort
from video_pipeline.domain.errors import UploadError
from video_pipeline.domain.models import PublishOptions

YOUTUBE_UPLOAD_SCOPE = "https://www.googleapis.com/auth/youtube.upload"
CATEGORY_EDUCATION = "27"


class YouTubeUploader(UploaderPort):
    """YouTube Data API v3. google-api-python-client は任意依存。"""

    def __init__(self, token_path: Path, client_secrets: Path | None = None) -> None:
        self._token_path = token_path
        self._client_secrets = client_secrets

    @classmethod
    def from_paths(
        cls,
        *,
        token_path: Path | None,
        client_secrets: Path | None = None,
    ) -> YouTubeUploader:
        if token_path is None:
            raise UploadError(
                "YouTube 資格情報がありません。local/youtube_token.json を置くか "
                "YOUTUBE_TOKEN_PATH を設定してください。"
            )
        return cls(token_path=token_path, client_secrets=client_secrets)

    def upload(self, video: Path, options: PublishOptions) -> str:
        if not video.is_file():
            raise UploadError(f"アップロードする動画がありません: {video}")
        if options.privacy not in {"private", "unlisted", "public"}:
            raise UploadError(f"不明な privacy: {options.privacy}")

        try:
            from google.oauth2.credentials import Credentials
            from googleapiclient.discovery import build
            from googleapiclient.http import MediaFileUpload
        except ImportError as exc:
            raise UploadError(
                "YouTube アップロードには google-api-python-client と google-auth が必要です。"
                " pip install -e '.[youtube]'"
            ) from exc

        creds = self._load_credentials(Credentials)
        try:
            youtube = build("youtube", "v3", credentials=creds, cache_discovery=False)
            body = {
                "snippet": {
                    "title": options.title,
                    "description": options.description,
                    "categoryId": CATEGORY_EDUCATION,
                },
                "status": {"privacyStatus": options.privacy},
            }
            media = MediaFileUpload(str(video), mimetype="video/mp4", resumable=True)
            request = youtube.videos().insert(part="snippet,status", body=body, media_body=media)
            response = None
            while response is None:
                _status, response = request.next_chunk()
        except UploadError:
            raise
        except Exception as exc:
            raise UploadError(f"YouTube アップロードに失敗しました: {exc}") from exc

        video_id = (response or {}).get("id")
        if not video_id:
            raise UploadError(f"YouTube が id を返しませんでした: {response}")
        return str(video_id)

    def _load_credentials(self, credentials_cls: type) -> object:
        if not self._token_path.is_file():
            raise UploadError(
                f"OAuth トークンがありません: {self._token_path}。"
                " YouTube Data API の OAuth クライアントで authorized-user JSON を保存してください。"
            )
        try:
            data = json.loads(self._token_path.read_text(encoding="utf-8"))
            return credentials_cls.from_authorized_user_info(data, scopes=[YOUTUBE_UPLOAD_SCOPE])
        except Exception as exc:
            raise UploadError(f"YouTube トークンを読めません: {exc}") from exc
