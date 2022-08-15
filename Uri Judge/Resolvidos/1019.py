a = int(input())
hora = int(a/60/60)
minuto = int((a - hora*60*60) / 60)
segundo = a%60
print(f"{hora}:{minuto}:{segundo}")