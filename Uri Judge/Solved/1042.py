a, b, c = map(int, input().split())
lista = [a, b, c]
lista.sort()

print(*lista, sep = "\n")
print(f"\n{a}\n{b}\n{c}")