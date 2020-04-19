# Extracting Data from XML

# http://py4e-data.dr-chuck.net/comments_42.xml
# http://py4e-data.dr-chuck.net/comments_398218.xml

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')
    #print(data)
    tree = ET.fromstring(data)

    counts = tree.findall('.//count') # XPath selector string
    c = list()
    counter = 0

    for item in counts:
        count = float(item.text)
        c.append(count)
        counter += 1

    print('Count: ', counter)
    print('Sum: ', sum(c))
