a = int(input())
ano = int(a/365)
mes = int((a - ano*365) / 30)
dia = a%365%30

print(f"{ano} ano(s)\n{mes} mes(es)\n{dia} dia(s)")