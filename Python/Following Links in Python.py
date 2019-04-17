import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
url = 'http://py4e-data.dr-chuck.net/known_by_Dailey.html'

#test
count = 4
position = 3

#submission
count = 7
position = 18

for i in range(0, count):
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    
    tag = tags[position-1]

    url = tag.get('href', None)
    content = tag.contents[0]
##    print ('TAG:',tag)
##    print ('URL:',tag.get('href', None))
##    print ('Contents:',tag.contents[0])
##    print ('Attrs:',tag.attrs)
print ('Last Name: ' + content)   



    
