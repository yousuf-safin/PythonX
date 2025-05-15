import os #importing os to get access of directory

directory_path = r'C:\Users\User\Downloads\Python\The-Ultimate-Python-Course-main' #ading the directory path
contents = os.listdir(directory_path)#listing the directory items

print(f"Contents of directory '{directory_path}':")#printing the file path directory
for item in contents:
    print(item)#printing each of the files and folders in the directory
