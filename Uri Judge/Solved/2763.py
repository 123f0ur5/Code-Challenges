import re

spt = re.compile('[-.]')
s = input()

a = spt.split(s)

for x in a:
    print(x)