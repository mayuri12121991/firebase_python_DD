import pyrebase
import os
import argparse

# Test App
# config = {
# 	    "apiKey": "AIzaSyDyBLVrI_OGBjKhpIlQYGQGsJTIP9Cmv7U",
#     	"authDomain": "dailydatatest.firebaseapp.com",
#     	"databaseURL": "https://dailydatatest.firebaseio.com",
#     	"projectId": "dailydatatest",
#     	"storageBucket": "dailydatatest.appspot.com",
#     	"messagingSenderId": "183350005160",
#     	"appId": "1:183350005160:web:9a749770a25b9c903e619d",
#     	"measurementId": "G-QWCD2D4PV0",
# 	    "serviceAccount": "/mnt/c/Users/soura/OneDrive/Ideas/Crowd_Data_Collection/firebase/firebase_key_test/dailydatatest-firebase-adminsdk-9wnx1-d80461a4c3.json"
# }

# Main App
"""
Steps to generate the apikey
- Create new web app in firebase project
- The apiKey will be present at the same page. OR web app -> settings -> General 
- Copy paste the complete code here i.e. apiKey to appId stuff
Steps to generate the apiKey Json file (serviceAccount)
- Goto the web app you created above
- web app -> settings -> Service Account -> Generate new private key 
"""

# Create config for your firebase project
config = {
	    "apiKey": "AIzaSyCEY8KNF9kMQ3BoRwT6C_CoO8CNTIberGs",
        "authDomain": "photoshare-35c59.firebaseapp.com",
        "databaseURL": "https://photoshare-35c59.firebaseio.com",
        "projectId": "photoshare-35c59",
        "storageBucket": "photoshare-35c59.appspot.com",
        "messagingSenderId": "200904414492",
        "appId": "1:200904414492:web:29eb0f5d3325b8178cd6d9",
	    "serviceAccount": "/mnt/c/Users/soura/OneDrive/Ideas/Crowd_Data_Collection/firebase/firebase_main_app_key/photoshare-35c59-firebase-adminsdk-zq4ht-9cc51f8087.json"
}

# Create fire object
firebase = pyrebase.initialize_app(config)

# Get storage
storage = firebase.storage()

# Parse user inputs
parser = argparse.ArgumentParser("Link firebase script")

parser.add_argument("-cd", "--cloud_dir", type=str, required=True, default="photos", help="Provide main cloud dir name")
parser.add_argument("-cs", "--cloud_subdir", type=str, required=True, default=None, help="Provide subdir name")
parser.add_argument("-ld", "--local_dir", type=str, required=False, default="/mnt/d/DataCluster_dataset/server/", help="Provide path on local dir to download stuff from cloud")

args = parser.parse_args()

local_dir = args.local_dir

if not args.cloud_subdir:
    print("Please provide subdir nmae. This is done for safety")
    exit()

path_on_cloud = args.cloud_dir + "/" + args.cloud_subdir + "/"
print("path on cloud: ", path_on_cloud)
all_fols = storage.child(path_on_cloud).list_files()

total_files = 0
for file in all_fols:
    print("filename: ", file.name)
    total_files  += 1
    print("Total_file approx: ", total_files)

    if path_on_cloud in str(file):
        file_name = "/" + file.name
        image_name = file.name.split("/")[-1]

        local_dir_fold = local_dir + path_on_cloud
        if not os.path.exists(local_dir_fold):
            print("Creating dir: ", local_dir_fold)
            os.makedirs(local_dir_fold)

        try:
            print("Downloading to : ", local_dir_fold + image_name)
            storage.child(file_name).download(local_dir_fold + image_name)
            # for file1 in all_files:
            #     print(local_dir + file.name)
            #     storage.child(file1.name).download(local_dir + file.name)
        except:
            print('Download Failed')