import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'
#address = 'South Federal University'
address = 'Monash University Churchill Australia'

url = serviceurl + urllib.parse.urlencode({'address' : address})

print('Retrieving', url)
data = urllib.request.urlopen(url).read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)
#print(json.dumps(js, sort_keys=True, indent=4, separators=(',', ': ')))

print('Place id', js['results'][0]['place_id'])
