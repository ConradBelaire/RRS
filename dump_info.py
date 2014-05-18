
import xml.etree.ElementTree as ET

tree = ET.parse('RoosterTeeth.xml')
root = tree.getroot()

print (root.tag)

for i in root.find('channel').findall('item'):
    print ("{title}: {url}".format(title=i.find('title').text,
                                   url=i.find('enclosure').get('url')))
