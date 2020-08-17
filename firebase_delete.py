import pyrebase
import os

config = {
    "apiKey": "AIzaSyB_v-SHm7MgQcEoqCai5uoiHa-Ck6eAokU",
    "authDomain": "uploadimage-ec821.firebaseapp.com",
    "databaseURL": "https://uploadimage-ec821.firebaseio.com",
    "projectId": "uploadimage-ec821",
    "storageBucket": "uploadimage-ec821.appspot.com",
    "messagingSenderId": "1025160577177",
    "appId": "1:1025160577177:web:cea64c8c4ff36764fa3808",
    "measurementId": "G-Q45LKF2KFD",
    "serviceAccount": "C:/Users/Administrator/uploadimage-ec821-firebase-adminsdk-6x1li-df65873911.json"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = "/Storage/TaskImage"

path_on_local = "C:/Users/Administrator/Pictures/firebase_downloaded/"
all_fols = storage.child(path_on_cloud).list_files()

for file in all_fols:
    print(file.name)

    if ".jpg" in str(file):
        folder_name = file.name.split("/")[-2]
        image_name = file.name.split("/")[-1]
        print("Folder name: ", folder_name)
        try:

            print("image: ", image_name)
            print("file: ",file.name)
            storage.child(file.name).delete(file.name)

        except:
            print('Delete Failed')