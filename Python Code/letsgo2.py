from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter - ')
html=urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print('Retrieved',len(soup), 'characters')

parts=soup('tr')
for part in parts:
    print(len(part))
    print(part.attrs)
    print(len(part.contents[0]))
    print(part.contents[0])


    print(part)
