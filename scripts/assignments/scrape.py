import urllib
from BeautifulSoup import *

url =  'http://python-data.dr-chuck.net/comments_213645.html' 

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

# Retrieve all span tags
tags = soup('span')

total = 0
count = 0
for tag in tags:
	# print comment
	number = int(tag.contents[0])
	total += number
	count += 1

print "Count: " + str(count)
print "Total: " + str(total)


