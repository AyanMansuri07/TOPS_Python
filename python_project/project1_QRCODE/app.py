# from flask import Flask, request
# import os
# from googleapiclient.discovery import build
# from googleapiclient.http import MediaFileUpload
# from google.oauth2 import service_account

# # Flask setup
# app = Flask(__name__)
# UPLOAD_FOLDER = 'uploads'
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# # Google Drive API setup
# SERVICE_ACCOUNT_FILE = 'credentials.json'  # downloaded from Google Cloud
# SCOPES = ['https://www.googleapis.com/auth/drive.file']

# credentials = service_account.Credentials.from_service_account_file(
#     SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# drive_service = build('drive', 'v3', credentials=credentials)

# # Replace with your folder ID from Google Drive
# FOLDER_ID = "1JEzQx4_UQhVspI6socpzyhDw9EbWJOLg"

# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'POST':
#         file = request.files['file']
#         if file:
#             filepath = os.path.join(UPLOAD_FOLDER, file.filename)
#             file.save(filepath)

#             # Upload to Google Drive
#             file_metadata = {
#                 'name': file.filename,
#                 'parents': [FOLDER_ID]
#             }
#             media = MediaFileUpload(filepath, resumable=True)
#             drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

#             return "<h2>✅ File uploaded successfully to Google Drive!</h2>"

#     return '''
#     <h1>Upload Your Photo or Data</h1>
#     <form method="post" enctype="multipart/form-data">
#         <input type="file" name="file" required>
#         <input type="submit" value="Upload">
#     </form>
#     '''

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)

from flask import Flask, request, redirect
import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Flask setup
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Google Drive API setup
SERVICE_ACCOUNT_FILE = 'credentials.json'  # downloaded from Google Cloud
SCOPES = ['https://www.googleapis.com/auth/drive.file']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Replace with your folder ID from Google Drive
FOLDER_ID = "1JEzQx4_UQhVspI6socpzyhDw9EbWJOLg"

@app.route('/')
def home():
    return redirect('/upload')  # Redirect to upload page

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)

            # Upload to Google Drive
            file_metadata = {
                'name': file.filename,
                'parents': [FOLDER_ID]
            }
            media = MediaFileUpload(filepath, resumable=True)
            drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()

            return "<h2>✅ File uploaded successfully to Google Drive!</h2>"

    return '''
    <h1>Upload Your Photo or Data</h1>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <input type="submit" value="Upload">
    </form>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
