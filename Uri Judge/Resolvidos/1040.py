a, b, c, d = map(float, input().split())
pesos = [2, 3, 4, 1]
notas = [a, b, c, d]
nota = 0
x = 0

for i in pesos:
    nota += pesos[x]*notas[x]
    x += 1

media = nota / 10

print("Media: {:.1f}".format(media))

if(media >= 7):
    print("Aluno aprovado.")
elif(media < 5):
    print("Aluno reprovado.")
elif(media >= 5 and media < 7):
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: {:.1f}".format(e))
    novanota = (media + e) / 2
    if(novanota < 5):
        print("Aluno reprovado.")
        print("Media final: {:.1f}".format(novanota))
    else:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(novanota))