a, b = map(float, input().split())

if(a == 0 and b == 0):
    print("Origem")
elif(a == 0 and b != 0):
    print("Eixo Y")
elif(a != 0 and b == 0):
    print("Eixo X")
elif min(a, b) > 0:
    print("Q1")
elif max(a, b) < 0:
    print("Q3")
elif(a < 0 and b > 0):
    print("Q2")
else:
    print("Q4")