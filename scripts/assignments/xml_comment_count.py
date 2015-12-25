import urllib
import xml.etree.ElementTree as ET

url = 'http://python-data.dr-chuck.net/comments_213642.xml'
print 'Retrieving: ', url

xml = urllib.urlopen(url).read()
print 'Retrieved', len(xml), 'characters'
# print xml

# Parse XML
tree = ET.fromstring(xml)

# get comments
comment = tree.findall('.//comment')
# print comment

# get count and add to array 
counts = []
for item in comment:
	count = item.find('count').text
	counts.append(count)

# compute sum
total = 0
for i in counts:
	total += int(i)

# print
print 'Count: ', len(counts)
print 'Total: ', total


