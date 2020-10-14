# import xml.etree.ElementTree
import xml.etree.ElementTree as ET
import glob
import os 


# Open original file
xml_list = []
# path = os.path.join(os.getcwd(), 'annotations')
for xml_file in glob.glob('data/hook_helmet_dataset/annotations/*.xml'):
    filename = xml_file.split('/')[-1]
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
  
        if member[0].text == 'hat':
            member[0].text = 'helmet'
        elif member[0].text == 'person':
            member[0].text = 'head'
    tree.write(f'annotations/{filename}')