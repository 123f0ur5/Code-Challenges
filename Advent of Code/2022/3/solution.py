#Part 1
from string import ascii_letters
total1 = 0

with open('input.txt', 'r') as inp: #Check if you're in the right repository on terminal
     values = inp.read().split('\n')

for value in values:
     index = int(len(value)/2)
     first = set(value[:index])
     second = set(value[index:])
     for letter in first:
          if letter in second:
               total1 += int(1 + ascii_letters.index(letter))

print(total1)

#Part 2

total2 = 0

for i in range(0, len(values), 3):
     badge = list(set(values[i]).intersection(set(values[i+1])).intersection(set(values[i+2])))
     total2 += 1 + ascii_letters.index(badge[0])

print(total2)