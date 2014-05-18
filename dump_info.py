
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

def parse_item(item):
	return {
		"title": item.find('title').text,
	    "url": item.find('enclosure').get('url'),
		"date": datetime.strptime(item.find('pubDate').text, "%a, %d %b %Y %H:%M:%S %Z")
	}


def main(filename, days_ago):	
	tree = ET.parse(filename)
	root = tree.getroot()

	all_items = [parse_item(i) for i in root.find('channel').findall('item')]
	new_items = [i for i in all_items if i["date"] > datetime.today() - timedelta(days=days_ago)]

	for i in new_items:
		print ("{date}\n{title}: {url}".format(**i))


main('RoosterTeeth.xml', 40)


