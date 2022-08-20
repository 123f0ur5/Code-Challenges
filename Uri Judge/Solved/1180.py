a = int(input())
menor = 999999999999999999999999999999999
pos = 0

vet = input().split()

for i in range(0,a):
    if(int(vet[i]) < menor):
        menor = int(vet[i])
        pos = i

print(f'Menor valor: {menor}\nPosicao: {pos}')