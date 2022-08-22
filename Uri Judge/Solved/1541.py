from math import sqrt

while True:
    a = input()
    if a ==  '0':
        break
    else:
        a, b, c = a.split()
        print(int(sqrt(int(a)*int(b) / int(c)/100)*100))