#import string
#string.ascii_letters.lower string.ascii_letters.upper
n = int(input())
res = []

for i in range(n):
    txt = input()
    new_txt = txt

    new_txt = map(ord, txt)
    new_txt = list(map(lambda x: x+3 if x >= 65 and x <= 90 or x >= 97 and x <= 122 else x, new_txt))
    new_txt = new_txt[::-1]
    new_txt = new_txt[:len(txt)//2] + list(map(lambda x: x-1, new_txt[len(txt)//2:]))
    new_txt = list(map(chr, new_txt))
    
    res.append(''.join(new_txt))

for x in range(len(res)):
    print(res[x])