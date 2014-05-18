"""For downloading all the podcasts"""

import xml.etree.ElementTree as ET
import os.path
import requests

from datetime import datetime, timedelta


def retrieve_url_into_file(url, filename):
    r = requests.get(url, stream=True)
    with open(filename, 'wb') as fd:
        for chunk in r.iter_content(512):
            fd.write(chunk)


def parse_item(item):
    """Takes a ElementTree node for <item>

    returns a dictionary with the title, date and url
    """
    return {
        "title": item.find('title').text,
        "url": item.find('enclosure').get('url'),
        "date": datetime.strptime(
            item.find('pubDate').text, "%a, %d %b %Y %H:%M:%S %Z")
    }


def main(filename, days_ago):
    """Takes the rss xml file, and how many days ago to stop looking"""
    tree = ET.parse(filename)
    root = tree.getroot()

    all_items = [parse_item(i) for i in root.find('channel').findall('item')]
    new_items = [i for i in all_items 
                 if i["date"] > datetime.today() - timedelta(days=days_ago)]

    for i in new_items:
        print ("{date}\n{title}: {url}".format(**i))
        url=i['url']
        retrieve_url_into_file(url, os.path.basename(url))



main('RoosterTeeth.xml', 10)
