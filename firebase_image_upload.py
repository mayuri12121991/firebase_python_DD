import pyrebase

config = {
                     "Service key of firebase"
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