
import xml.etree.ElementTree as ET
tree = ET.parse('RoosterTeeth.xml')
root = tree.getroot()

print(root.tag)