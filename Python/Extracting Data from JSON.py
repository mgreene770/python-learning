import json
import urllib.request, urllib.parse, urllib.error

#Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_8581.json (Sum ends with 78)

#url = 'http://py4e-data.dr-chuck.net/comments_42.json'
url = 'http://py4e-data.dr-chuck.net/comments_8581.json'

print('Retrieving', url)
data = urllib.request.urlopen(url).read().decode()

print('Retrieved', len(data), 'characters')
js = json.loads(data)
#print(json.dumps(js, sort_keys=True, indent=4, separators=(',', ': ')))

item_count = 0
item_sum= 0
for item in js["comments"]:
    item_count = item_count + 1
    item_sum = item_sum + int(item["count"])
    #print(item)

print('Count:', item_count)
print('Sum:', item_sum)
