import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("severaccountkey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

collection_ref = db.collection("PU")
docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).limit(3).get()
for doc in docs:
    print("文件內容：{}".format(doc.to_dict()))
