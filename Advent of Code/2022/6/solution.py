cont = 4

with open('input.txt', 'r') as inp: #Check if you're in the right repository on terminal
     value = inp.read()

for i in range(len(value)):
    check = set(value[i:i+4])
    if len(check) == 4:
        break
    else:
        cont += 1

print(cont)