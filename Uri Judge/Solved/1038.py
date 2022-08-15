valores = [4, 4.5, 5, 2, 1.5]
a, b = map(int, input().split())
a -= 1

print("Total: R$ {:.2f}".format((valores[a]*b)))