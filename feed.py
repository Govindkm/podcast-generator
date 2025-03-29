import yaml
import xml.etree.ElementTree as xml_tree

with open('feed.yaml', 'r') as file:
    data = yaml.safe_load(file)
    rss_feed_element = xml_tree.Element('rss', version='2.0', attrib={
        'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
        'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
    })
    channel_element = xml_tree.SubElement(rss_feed_element, 'channel')

    # Add basic channel elements
    xml_tree.SubElement(channel_element, 'title').text = data['title']
    xml_tree.SubElement(channel_element, 'description').text = data['description']
    xml_tree.SubElement(channel_element, 'language').text = data['language']
    xml_tree.SubElement(channel_element, 'itunes:subtitle').text = data['subtitle']
    xml_tree.SubElement(channel_element, 'itunes:author').text = data['author']

    # Add image element
    if 'image' in data:
        image_element = xml_tree.SubElement(channel_element, 'itunes:image', href=data['image'])

    # Add category element
    if 'category' in data:
        xml_tree.SubElement(channel_element, 'itunes:category', text=data['category'])

    # Add items
    for item in data.get('item', []):
        item_element = xml_tree.SubElement(channel_element, 'item')
        xml_tree.SubElement(item_element, 'title').text = item['title']
        xml_tree.SubElement(item_element, 'description').text = item['description']
        xml_tree.SubElement(item_element, 'pubDate').text = item['published']
        xml_tree.SubElement(item_element, 'enclosure', attrib={
            'url': item['file'],
            'type': data['format'],
            'length': str(item['length'])
        })
        xml_tree.SubElement(item_element, 'itunes:duration').text = item['duration']

output_tree = xml_tree.ElementTree(rss_feed_element)
output_tree.write('feed.xml', encoding='utf-8', xml_declaration=True)