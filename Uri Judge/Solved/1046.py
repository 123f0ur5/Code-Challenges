a, b = map(int, input().split())
hora = 0
loop = False

if(a == b):
    print("O JOGO DUROU 24 HORA(S)")  

while(a != b):
    loop = True
    hora += 1
    a += 1
    if(a == 24):
        a = 0

if loop: 
    print(f"O JOGO DUROU {hora} HORA(S)")