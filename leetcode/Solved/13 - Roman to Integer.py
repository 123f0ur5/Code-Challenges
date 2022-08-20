a = input()
        
valores = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
    "IV" : 4,
    "IX" : 9,
    "XL" : 40,
    "XC" : 90,
    "CD" : 400,
    "CM" : 900,
}

valor = 0
j = 1

for i in range(len(a)):
    if(j < len(a)):
        if(a[i]+a[j] in valores):
            valor += valores.get(a[i]+a[j])
            valor -= valores.get(a[i])
            valor -= valores.get(a[j])
    if(a[i] in valores):
        valor += valores.get(a[i])
    j += 1

print(valor)