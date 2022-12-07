#Part 1
highest = 0
soma1 = 0

with open('input.txt', 'r') as inp: #Check if you're in the right repository on terminal
    values = inp.read().split('\n')


for value in values:
    if value == '':
        if soma1 > highest:
            highest = soma1

        soma1 = 0
    else:
        soma1 += int(value)

print(highest)

#Part 2
top3 = [0,0,0]
soma = 0

for value in values:
    if value == '':
        if soma > min(top3):
            top3.remove(min(top3))
            top3.append(soma)

        soma = 0
    else:
         soma += int(value)

print(sum(top3))