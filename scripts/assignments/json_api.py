import urllib
import json

# input api url
serviceurl = 'http://python-data.dr-chuck.net/geojson?'

# input address
address = 'University of Colorado at Boulder'

# construct api url and read json from it
url = serviceurl + urllib.urlencode({'sensor':'false', 'address': address})
print 'Retrieving', url
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved',len(data),'characters'

try: 
	js = json.loads(str(data))
except: 
	js = None

# print data
# print json.dumps(js, indent=4)
place_id = js['results'][0]['place_id']
print 'Place ID', place_id


