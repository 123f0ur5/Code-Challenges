while True:
    zero = 0; um = 0; dois = 0; tres = 0; quatro = 0; cinco = 0; seis = 0; sete = 0; oito = 0; nove = 0
    a, b = map(int, input().split())
    if a == b == 0:
        break  

    for i in range(b-a+1):
        a = str(a)
        for x in range(len(str(a))):
            if('0' in str(a[x])):
                zero += 1
            if('1' in str(a[x])):
                um += 1
            if('2' in str(a[x])):
                dois += 1
            if('3' in str(a[x])):
                tres += 1
            if('4' in str(a[x])):
                quatro += 1
            if('5' in str(a[x])):
                cinco += 1
            if('6' in str(a[x])):
                seis += 1
            if('7' in str(a[x])):
                sete += 1
            if('8' in str(a[x])):
                oito += 1
            if('9' in str(a[x])):
                nove += 1
        a = int(a) + 1
    print(f"{zero} {um} {dois} {tres} {quatro} {cinco} {seis} {sete} {oito} {nove}")