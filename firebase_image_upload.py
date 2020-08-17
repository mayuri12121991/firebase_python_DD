import pyrebase

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

firebase=pyrebase.initialize_app(config)
storage=firebase.storage()

path_on_cloud = "/Storage/TaskImage/AAA00"

path_on_local = "C:/Users/Administrator/Pictures/firebase_downloaded/"
all_files = storage.child(path_on_cloud).list_files()
for file in all_files:
    try:
        # file.download_to_filename(path_on_local + file.name)
        storage.child(file.name).download(path_on_local + file.name)
    except:
        print('Download Failed')