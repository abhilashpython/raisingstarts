import google
import urllib
#import re
from bs4 import BeautifulSoup
res = urllib.urlopen("https://docs.python.org/3.1/howto/urllib2.html")
data = res.read()
#print re.findall('<head>[.*?]</head>',data)
soup = BeautifulSoup(data, 'html.parser')
print soup
print type(soup)
#print soup.title.name
#for i in google.search("python"):
#	print i
