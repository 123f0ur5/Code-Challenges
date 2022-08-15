g = True
vi = 0; vg = 0; tie = 0

while g:
    gi, gg = map(int, input().split())
    if gi == gg:
        tie += 1
    elif(gi > gg):
        vi += 1
    else:
        vg += 1
    
    while True:
        cont = int(input('Novo grenal (1-sim 2-nao)\n'))

        if cont == 1:
            break
        elif cont == 2:
            g = False
            break

if(vi == vg):
    venc = 'Nao houve vencedor'
elif vi > vg:
    venc = 'Inter venceu mais'
else:
    venc = 'Gremio venceu mais'

print(f'{vi+vg+tie} grenais\nInter:{vi}\nGremio:{vg}\nEmpates:{tie}\n{venc}')