import pandas as pd
import xlrd
from shutil import copy
import os

current_path = os.getcwd()
print(current_path)

# create destination folder for malware data
malware_path='malware'
try:
    os.mkdir(malware_path)
except OSError:
    print ("Creation of the directory %s failed" % malware_path)
else:
    print ("Successfully created the directory %s " % malware_path)

# create destination folder for normal data
normal_path='normal'
try:
    os.mkdir(normal_path)
except OSError:
    print ("Creation of the directory %s failed" % normal_path)
else:
    print ("Successfully created the directory %s " % normal_path)

# create folder with data for testing
data_path='data'
try:
    os.mkdir(data_path)
except OSError:
    print ("Creation of the directory %s failed" % data_path)
else:
    print ("Successfully created the directory %s " % data_path)

# read file
data=pd.read_excel(os.path.join(current_path,'data.xlsx'), header=None)

# for test, create the files
for i, row in data.iterrows():
    f=open(os.path.join(current_path, data_path, './{}'.format(row[0])),"w+")
    f.write(row[0])
    f.close()

# move files
for i, row in data.iterrows():
    file_path=os.path.join(data_path,row[0])
    if row[1]==1:
        copy(file_path, malware_path)
    elif row[1]==0:
        copy(file_path, normal_path)