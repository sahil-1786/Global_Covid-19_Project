from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re


#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter - ')
html=urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print('Retrieved',len(soup), 'characters')


parts=soup('tr')
for part in parts[1:]:
    print(len(part))
    print(part )
    t=re.findall('^<td>(.+?)<',str(part.contents[0]))
    print(t)
    x=re.findall('^<td>(.+?)<',str(part.contents[1]))
    print(x)
    y=re.findall('^<td>(.+?)<',str(part.contents[2]))
    print(y)
    z=re.findall('^<td>(.+?)<',str(part.contents[3]))
    print(z)
    p=re.findall('^<td>(.+?)<',str(part.contents[4]))
    print(p)
print(len(parts))
