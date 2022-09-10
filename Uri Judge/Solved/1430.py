lst = ['W', 'H', 'Q', 'E', 'S', 'T', 'X']
notes = {y : 1/pow(2,x) for x, y in enumerate(lst)}

while True:
    s = input()
    if s == '*':
        break
    s = s.split('/')
    s.pop(0)
    s.pop(len(s)-1)

    ans = []

    for x, y in enumerate(s):
        note = 0
        for z in y:
            note += notes[z]
        ans.append(note)
    
    print(ans.count(1.0))