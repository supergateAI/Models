# import xml.etree.ElementTree
import xml.etree.ElementTree as ET
import glob
import os 


# Open original file
filename_list = []
# path = os.path.join(os.getcwd(), 'annotations')
for xml_file in glob.glob('annotations/*.xml'):
    filename = xml_file.split('/')[-1].split('.')[0]
    filename_list.append(filename)

with open("trainval.txt", "w") as file:
    for name in filename_list:
        file.write(name+"\n")
