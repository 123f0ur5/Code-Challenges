a, b, c = input().split()
print("TRIANGULO: {:.3f}".format(float(a)*float(c)/2))
print("CIRCULO: {:.3f}".format(3.14159*pow(float(c),2)))
print("TRAPEZIO: {:.3f}".format(((float(a)+float(b))*float(c))/2))
print("QUADRADO: {:.3f}".format(float(b)*float(b)))
print("RETANGULO: {:.3f}".format(float(a)*float(b)))