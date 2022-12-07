#Part 1
total1 = 0
choices = {
     'X' : 1,
     'Y' : 2,
     'Z' : 3
}

oponent = {
     'A' : 'X',
     'B' : 'Y',
     'C' : 'Z'
}

with open('input.txt', 'r') as inp: #Check if you're in the right repository on terminal
     values = inp.read().split('\n')

for value in values:
     total1 += choices[value[2]]

     if value[2] == oponent[value[0]]:
          total1 += 3
     if (value[2] == 'X' and oponent[value[0]] == 'Z') or (value[2] == 'Y' and oponent[value[0]] == 'X') or (value[2] == 'Z' and oponent[value[0]] == 'Y'):
          total1 += 6
     
print(total1)

#Part 2
total2 = 0

choice_draw = {
     'A' : 1,
     'B' : 2,
     'C' : 3
}

choice_win = {
     'A' : 2,
     'B' : 3,
     'C' : 1
}

choice_lose = {
     'A' : 3,
     'B' : 1,
     'C' : 2
}

for value in values:
     if value[2] == 'X':
          total2 += choice_lose[value[0]]
     elif value[2] == 'Y':
          total2 += 3
          total2 += choice_draw[value[0]]
     elif value[2] == 'Z':
          total2 += 6
          total2 += choice_win[value[0]]

print(total2)