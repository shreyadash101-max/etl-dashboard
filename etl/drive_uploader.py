import os
from pathlib import Path
from dotenv import load_dotenv

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/drive.file"]


def get_drive_service():

    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file(
            "token.json",
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json",
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open("token.json", "w") as token:
            token.write(creds.to_json())

    return build(
        "drive",
        "v3",
        credentials=creds
    )


def upload_reports():

    folder_id = os.getenv("DRIVE_FOLDER_ID")

    if not folder_id:
        raise ValueError(
            "DRIVE_FOLDER_ID is missing from .env"
        )

    service = get_drive_service()

    reports_folder = Path("reports")

    if not reports_folder.exists():
        raise FileNotFoundError(
            "The reports folder does not exist."
        )

    for file_path in reports_folder.iterdir():

        if file_path.is_file():

            query = (
                f"name = '{file_path.name}' "
                f"and '{folder_id}' in parents "
                f"and trashed = false"
            )

            results = service.files().list(
                q=query,
                spaces="drive",
                fields="files(id, name)"
            ).execute()

            existing_files = results.get("files", [])

            media = MediaFileUpload(
                str(file_path),
                resumable=True
            )

            if existing_files:

                file_id = existing_files[0]["id"]

                service.files().update(
                    fileId=file_id,
                    media_body=media
                ).execute()

                print(
                    f"Updated Google Drive file: "
                    f"{file_path.name}"
                )

            else:

                file_metadata = {
                    "name": file_path.name,
                    "parents": [folder_id]
                }

                service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields="id, name"
                ).execute()

                print(
                    f"Uploaded new Google Drive file: "
                    f"{file_path.name}"
                )

    print("Google Drive reports synchronized successfully.")