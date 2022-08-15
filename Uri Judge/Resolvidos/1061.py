from datetime import timedelta
from time import time

diaInicio = input().split('Dia')
horaInicio, minutoInicio, segundoInicio = map(int,input().split(':'))

diaFim = input().split('Dia')
horaFim, minutoFim, segundoFim = map(int,input().split(':'))

diaInicio = int(diaInicio[1])
diaFim = int(diaFim[1])

inicio = timedelta(days = diaInicio, hours = horaInicio, minutes = minutoInicio, seconds = segundoInicio)
fim = timedelta(days = diaFim, hours = horaFim, minutes = minutoFim, seconds = segundoFim)

print(f"{((fim-inicio).days)} dia(s)\n{(fim-inicio).seconds//3600} hora(s)")
print(f"{(fim-inicio).seconds//60%60} minuto(s)\n{(fim-inicio).seconds - ((((fim-inicio).seconds//3600)*3600)+((fim-inicio).seconds//60%60)*60)} segundo(s)")