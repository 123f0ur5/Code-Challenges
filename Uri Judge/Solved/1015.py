import math
a, b = map(float, input().split())
c, d = map(float, input().split())
print("{:.4f}".format(math.sqrt(pow((a-c),2)+pow((d-b),2))))