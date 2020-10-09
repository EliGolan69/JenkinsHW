import shutil
import os

from_file_name = os.environ["HOMEPATH"] + "\Desktop\MyName.txt"
to_file_name = "c:\Python\MyName.txt"
if os.path.exists(from_file_name):
   shutil.move(from_file_name, to_file_name)