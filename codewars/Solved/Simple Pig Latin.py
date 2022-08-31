import string

def pig_it(text):
    new = list(text.split())
    ans = []
    for x in new:
        if x not in string.punctuation:
            x = x[1:] + x[0::-1] + 'ay'
            ans.append(x)
        else:
            ans.append(x)
    
    return ' '.join(ans)

ans = pig_it('Pig latin is cool') # 'igPay atinlay siay oolcay'
print(ans)