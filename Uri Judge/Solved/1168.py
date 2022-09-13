dct = {
    '1' : 2,
    '2' : 5,
    '3' : 5,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 3,
    '8' : 7,
    '9' : 6,
    '0': 6,
}

n = int(input())

for i in range(n):
    sum = 0
    s = input()

    for x in s:
        sum += dct[x]
    
    print(f'{sum} leds')