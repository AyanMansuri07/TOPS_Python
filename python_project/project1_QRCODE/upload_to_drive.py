from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

# Authenticate using service account
SERVICE_ACCOUNT_FILE = 'C:\Users\Ayan\OneDrive\Desktop\TOPS_Python\python_project\project1_QRCODE\credentials.json'

SCOPES = ['https://www.googleapis.com/auth/drive']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

service = build('drive', 'v3', credentials=credentials)

# Your file details
file_path = 'example.png'  # Path to your file
filename = 'example.png'   # File name in Google Drive
folder_id = '1JEzQx4_UQhVspI6socpzyhDw9EbWJOLg'  # Replace with your actual folder ID

# Add file metadata including folder
file_metadata = {
    'name': filename,
    'parents': ['1JEzQx4_UQhVspI6socpzyhDw9EbWJOLg']  # This will upload file inside specific folder
}

media = MediaFileUpload(file_path, mimetype='image/png')

# Upload file
file = service.files().create(body=file_metadata, media_body=media, fields='id').execute()

print(f"File uploaded successfully. File ID: {file.get('id')}")
