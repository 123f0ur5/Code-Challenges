#Part 1

total1 = 0

with open('input.txt', 'r') as inp: #Check if you're in the right repository on terminal
     values = inp.read().split('\n')

for value in values:
    x1, x2, y1, y2 = map(int, value.replace(',','-').split('-'))

    
    if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2):
        total1 += 1

print(total1)

#Part 2

total2 = 0

for value in values:
    x1, x2, y1, y2 = map(int, value.replace(',','-').split('-'))
    if (x1 <= y1 and x2 >= y2) or (y1 <= x1 and y2 >= x2) or \
    (x1 in range(y1,y2) or x2 in range(y1,y2) or y1 in range(x1,x2) or y2 in range(x1,x2)): # Note: Try to improve that part
        total2 += 1

print(total2)