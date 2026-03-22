from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re
import sqlite3


#Ignore SSL Certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode=ssl.CERT_NONE

url = input('Enter - ')
if len(url)<1:
    url='https://coronavirus.jhu.edu/data/mortality'
html=urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#create connection object
conn=sqlite3.connect('corona.sqlite')
#create cursor object
cur=conn.cursor()

#SQL Tables
cur.executescript('''
DROP TABLE IF EXISTS CoronaData;


CREATE TABLE CoronaData(
country TEXT UNIQUE,
confirmed INTEGER,
deaths INTEGER,
case_fatality TEXT,
deaths_per100kpop float
)
''')
#Use Regular Expressions to pull our data
parts=soup('tr')
for part in parts[1:]:
    t=re.findall('^<td>(.+?)<',str(part.contents[0]))

    x=re.findall('^<td>(.+?)<',str(part.contents[1]))

    y=re.findall('^<td>(.+?)<',str(part.contents[2]))

    z=re.findall('^<td>(.+?)<',str(part.contents[3]))

    p=re.findall('^<td>(.+?)<',str(part.contents[4]))

# Got some issues with INTEGER numbers and i had to replace commas,
# because python wants 1000 instead of 1,000
    country = t[0]
    confirmed = int(x[0].replace(',', ''))
    deaths = int(y[0].replace(',', ''))
    case_fatality = z[0]
    deaths_per100kpop = float(p[0])

    cur.execute('''INSERT OR IGNORE INTO CoronaData
    (country,confirmed,deaths,case_fatality,deaths_per100kpop)
    VALUES(?,?,?,?,?)''',
    (country,confirmed,deaths,case_fatality,deaths_per100kpop))

conn.commit()
