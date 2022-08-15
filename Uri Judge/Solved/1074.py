a = int(input())

for i in range(0,a):
    b = int(input())
    if b == 0:
        print("NULL")
    elif(b%2==0):
        print("EVEN", end='')
    else:
        print("ODD", end='')
    if(b>0):
        print(" POSITIVE")
    elif(b < 0):
        print(" NEGATIVE")