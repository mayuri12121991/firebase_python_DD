import pyrebase
import os

config = {
    "service key of firebase"
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