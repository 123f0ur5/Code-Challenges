import os

x = input("Folder name: ")

os.mkdir(x)
f = open(f'{x}/description.txt', "x")
f.close()
f = open(f'{x}/input.txt', "x")
f.close()
f = open(f'{x}/solution.py', "x")
f.close()