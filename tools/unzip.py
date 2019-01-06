import os
import zipfile
import shutil
import argparse

from pathlib import PurePath

parser = argparse.ArgumentParser(description="parameters")
parser.add_argument("dir", default="./", help="direcotry which contains zipfiles")
args = parser.parse_args()

dir = args.dir
files = os.listdir(dir)

#make directory for zip files and extracted files
os.makedirs('./zipfiles', exist_ok=True)
os.makedirs('./input', exist_ok=True)

#extract zipfiles in current directory and move zipfiles to zipfiles direcotry
for file in files:
    try:
        with zipfile.ZipFile(str(PurePath(dir,file))) as existing_zip:
            existing_zip.extractall('./input/')
        shutil.move(str(PurePath(dir,file)), './zipfiles')
    except:
        pass
