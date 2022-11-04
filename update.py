mport firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection("PU")
docs = collection_ref.where("lab","==", 579).get()
NewData = {"name": "子青老師"}
for doc in docs:
    doc_ref = db.collection("PU").document(doc.id)
    doc_ref.update(NewData)
