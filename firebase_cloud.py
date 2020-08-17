import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

/
cred = credentials.Certificate("C:/Users/PALASH/Downloads/uploadimage-ec821-firebase-adminsdk-6x1li-2dfb3a4142.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

# doc_ref = db.collection('ALL_IMAGES').document('nxlqrnxlzqcwr3iz5OHn')
#
# doc_ref.set({
#
#     'name':'mayuri',
#     'lname':'malviya',
#     'phone':'7829963267'
# })

img_ref = db.collection('ALL_IMAGES')
docs = img_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id,doc.to_dict()))
