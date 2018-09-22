import os
import zipfile
import shutil

files = os.listdir('./')

#make directory for zip files
os.makedirs('./zipfiles', exist_ok=True)

#extract zipfiles in current directory and move zipfiles to zipfiles direcotry
for file in files:
    try:
        with zipfile.ZipFile('./'+file) as existing_zip:
            existing_zip.extractall('./')
        shutil.move('./'+file, './zipfiles')
    except:
        pass
