# Following Links in HTML Using BeautifulSoup

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# http://py4e-data.dr-chuck.net/known_by_Fikret.html
# http://py4e-data.dr-chuck.net/known_by_Sylvia.html

url = input('Enter - ')
count = int(input('Enter count: '))
pos = int(input('Enter position: ')) - 1

# Retrieve all of the anchor tags
urllist = list()

for i in range(count):

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    print('Retrieveing:',url)

    taglist = list()

    for tag in tags:
        x = tag.get('href', None)
        taglist.append(x)

    url = taglist[pos]

    urllist.append(url)

print("Last Url:",urllist[-1])
