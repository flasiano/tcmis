import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("severaccountkey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc = {
  "name": "mjie",
  "mail": "s1101687@pu.edu.tw",
  "lab": 579
}
docs = [
{
  "name": "陳武林",
  "mail": "wlchen@pu.edu.tw",
  "lab": 665
},
{
  "name": "莊育維",
  "mail": "ywchuang@pu.edu.tw",
  "lab": 566
},

{
  "name": "汪于茵",
  "mail": "yywang13@pu.edu.tw",
  "lab": 674
}

]


#doc_ref = db.collection("PU").document("mjie")
#doc_ref.set(doc)
collection_ref = db.collection("PU")
for doc in docs:
 collection_ref.add(doc)
