import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# http://py4e-data.dr-chuck.net/comments_398219.json (Sum ends with 79)
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

while True:

    url = input('Enter location: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    c = list()
    counter = 0

    for item in js['comments']:
        count = item['count']
        name = item['name']

        count = float(count)
        c.append(count)
        counter += 1

    print('Count: ', counter)
    print('Sum: ', sum(c))
