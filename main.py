import os

file_name = os.environ["HOMEPATH"] + "\Desktop\MyName.txt"

text_file = open(file_name, 'w')
text_file.write('Eli Golan')
text_file.close()
