a = int(input())
somain = 0
somaout = 0

for i in range(0, a):
    b = int(input())
    if(b >= 10 and b <= 20):
        somain += 1
    else:
        somaout += 1
    
print(f"{somain} in\n{somaout} out")