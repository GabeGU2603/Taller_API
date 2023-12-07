import firebase_admin
from firebase_admin import credentials,firestore_async, storage

cred_firebase = credentials.Certificate("speakscope-frontend-d7e24-firebase-adminsdk-863oj-7d6bb3f8d5.json")

firebase_admin.initialize_app(cred_firebase)
