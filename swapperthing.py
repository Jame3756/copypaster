import os
import shutil
path="C:/Users/Member/Documents/Downloads/PyProjects/things im forced to do/something I already did but have to do again/files"
print("before copying file: ")
print(os.listdir(path))
source="C:/Users/Member/Documents/Downloads/PyProjects/things im forced to do/something I already did but have to do again/files/copy.txt"
destination="C:/Users/Member/Documents/Downloads/PyProjects/things im forced to do/something I already did but have to do again/files/paste.txt"
dest = shutil.copy(source, destination)
print("After copying file:")
print(os.listdir(path))