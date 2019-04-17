import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = 'http://py4e-data.dr-chuck.net/comments_42.xml'
url = 'http://py4e-data.dr-chuck.net/comments_8580.xml'

opener = urllib.request.build_opener()
tree = ET.parse(opener.open(url))
counts = tree.findall('.//count')
total_count = 0
print ('Count:', len(counts))
for c in counts:
    #print (c.text)
    total_count = total_count + int(c.text)

print('Sum:', total_count)

