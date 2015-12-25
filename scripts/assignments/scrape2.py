import urllib
from BeautifulSoup import *
import json
import ssl

url = 'https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Allice.html '
print 'Retrieving: ', url

count = 7
position = 18
indicator = 0

while indicator < count:
	scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
	uh = urllib.urlopen(url, context=scontext)
	html = uh.read()
	soup = BeautifulSoup(html)
	tags = soup('a')

	url_links = []
	for tag in tags:
		link = tag.get('href', None)
		url_links.append(str(link))
	url = url_links[position-1]
	print "Retrieving: ", url
	indicator+=1
















	



