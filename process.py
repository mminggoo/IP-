import os
from PIL import Image
from glob import glob

def delete_invalid_files(files):
    for file in files:
        file_path = file
        try:
            with Image.open(file_path) as img:
                continue
        except:
            os.remove(file_path)

        os.remove(file_path)

files = glob('images/*')
delete_invalid_files(files)
