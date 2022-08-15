import math
a, b, c = map(float, input().split())
delta = (pow(b,2)-4*a*c)
if 0 in (a, b, c) or delta < 0:
    print("Impossivel calcular")
else:
    print("R1 = {:.5f}".format(((-b+math.sqrt(delta))/(2*a))))
    print("R2 = {:.5f}".format(((-b-math.sqrt(delta))/(2*a))))