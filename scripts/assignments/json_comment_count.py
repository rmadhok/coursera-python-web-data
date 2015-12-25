import urllib
import json

# Get url containing json
url = 'http://python-data.dr-chuck.net/comments_213646.json'
print 'Retrieving', url

# load json data
uh = urllib.urlopen(url)
data = uh.read()
js = json.loads(str(data))

# Count
print 'Retrieved ' + str(len(data)) + ' characters'
counts = []
for item in js['comments']:
	counts.append(item['count'])

# Sum
print 'Count:', len(counts)
total = 0
for i in counts:
	total += i
print 'Total:', total




	