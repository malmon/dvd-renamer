import requests
import os
import shutil
from time import sleep

source_dir = '/source'
destination_dir = '/destination'
dump_dir = '/trash'
file_extention = '.mkv'
apikey = os.environ.get('APIKEY')
print("Starting DVD Renamer")
while True:
    for file in os.listdir(source_dir):
        if file.endswith(file_extention):
            source_file = os.path.join(source_dir, file)
            print("Found file {}".format(source_file))
            r = requests.get('http://www.omdbapi.com/?apikey={}&t={}'.format(apikey, os.path.splitext(file)[0].replace(' ','+').replace('_','+')))
            if r.status_code == 200:
                json_data = r.json()
                dest_str = '{} ({})'.format(json_data['Title'], json_data['Year'])
                if os.path.exists(os.path.join(destination_dir, dest_str)):
                    destination_path = os.path.join(dump_dir, dest_str)
                    print("Directory Already Exists Moving To Dumping Dir For Manual Processing")
                else:
                    destination_path = os.path.join(destination_dir, dest_str)
                destination_file = os.path.join(destination_path, '{}{}'.format(dest_str, file_extention))
                print("Moving File {} to {}".format(source_file, destination_file))
                os.mkdir(destination_path)
                shutil.move(source_file, destination_file)
    sleep(10)