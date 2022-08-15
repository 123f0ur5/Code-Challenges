def narcissistic(value):
    sum = 0
    tam = len(value)
    for x in value:
        sum += pow(int(x),tam)
    
    if(sum == int(value)):
        return True
    else:
        return False


a = str(input())

narcissistic(a)