import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccount.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

all_posts = []

def create_post(name, content):
    doc_ref = db.collection(u'posts').document()
    doc_ref.set({
        'name': name,
        'content': content
    })

def read_posts():
    posts = db.collection(u'posts').stream()
    for post in posts:
        all_posts.append(post.to_dict())

def get_posts():
    return all_posts