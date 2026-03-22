import re

text='<td>New Zealand</td>'

x=re.findall('^<td>(.+?)<',text)
print(x)
print(re.findall('^<td>(.+?)<',text))
