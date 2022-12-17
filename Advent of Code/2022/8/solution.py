import re
from math import ceil

with open('input.txt', 'r') as inp: #Check if you're in the right repository on terminal
     values = inp.read().split('\n')

mat = []
for value in values:
    line = re.findall('\d', value)
    mat.append(line)

total = len(mat) * 4 - 4

for i in range(1,len(mat)-1):
     highestleft = int(mat[i][0])
     highestright = int(mat[i][len(mat)-1])
     for j in range(1,(len(mat)-1)//2):
          if int(mat[i][j]) > highestleft:
               total += 1
               highestleft = int(mat[i][j])
          if int(mat[i][len(mat)-j-1]) > highestright:
               total += 1
               highestright = int(mat[i][j])
     if len(mat)/2!=0:
          if int(mat[i][int(len(mat)/2)]) > highestleft or int(mat[i][int(len(mat)/2)]) > highestright:
               total += 1

print(total)