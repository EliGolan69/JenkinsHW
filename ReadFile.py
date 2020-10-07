import os

file_name = os.environ["HOMEPATH"] + "\Desktop\MyName.txt"

text_file = open(file_name, 'r')
file_data = text_file.readline()
print(file_data)
text_file.close()
