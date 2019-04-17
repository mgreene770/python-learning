import urllib.request, urllib.parse, urllib.error
import ssl
import re
from bs4 import BeautifulSoup

def crawl(url):
    print('crawl (url):', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    print('html', html)
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        ref = tag.get('href', None)
        print('ref: ', ref)
        #crawl(urllib.request.urlopen(ref).read())
        #crawl(ref)
        
#url = input('Enter - ')
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://www.dr-chuck.com/page1.htm'
url = '<p>Please click <a href="http://www.dr-chuck.com">here</a></p>'

print('Search:', re.findall('href="(.+)"', url))
print('Search:', re.findall('href=".+"', url))
print('Search:', re.findall('href=//.*', url))
print('Search:', re.findall('<.*>', url))

#crawl(url)
#soup = BeautifulSoup(html, 'html.parser')

#print('children', soup.children)
#for child in soup.children:
#    print('child', child)
    

#tags = soup('a')
#print('tags', tags)
#for tag in tags:
#    print(tag.get('href', None))


    
