import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://maps.googleapis.com/maps/api/geocode/json?'

while True:
    #address = input('Enter location: ')
    address = '3535 Piedmont Road, Atlanta, GA 30005'
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address' : address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('=== Failure to Retrieve ===')
        print(data)
        continue

    loc = js["results"][0]["geometry"]["location"]
    lat = loc["lat"]
    lng = loc["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    print(json.dumps(js, sort_keys=True, indent=4, separators=(',', ': ')))

    break
    
##input = '''
##[
##    { "id" : "001",
##      "x": "2",
##      "name" : "chuck"
##    },
##    { "id" : "009",
##      "x": "7",
##      "name" : "Chuck"
##    }
##]'''
##
##info = json.loads(input)
##
##print('User count:', len(info))
##for item in info:
##    print('Name', item["name"])
##    print('Id', item["id"])
##    print('Attribute', item["x"])
