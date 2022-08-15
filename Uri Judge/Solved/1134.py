c = 0
alcool = 0; gas = 0; diesel = 0

while c != 4:
    c = int(input())

    if c == 1:
        alcool += 1
    elif c == 2:
        gas += 1
    elif c == 3:
        diesel += 1

print(f'MUITO OBRIGADO\nAlcool: {alcool}\nGasolina: {gas}\nDiesel: {diesel}')