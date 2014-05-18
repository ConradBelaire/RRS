import xml.etree.ElementTree as ET
tree = ET.parse('RootserTeeth.xml')
root = tree.getroot()

print(root)