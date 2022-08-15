a, b, c = map(float, input().split())

if(((b-c) < a) and (a < (b+c)) and ((a-c) < b) and (b < (a+c)) and ((a-b) < c) and (c < (a+b))):
    print("Perimetro = {:.1f}".format((a+b+c)))
else:
    print("Area = {:.1f}".format((a*c+b*c)/2))