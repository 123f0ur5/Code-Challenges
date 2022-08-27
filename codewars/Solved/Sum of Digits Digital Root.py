def digital_root(n):
    soma = 0
    for x in str(n):
        soma += int(x)
    if soma < 10:
        return soma
    else:
        return digital_root(soma)


ans = digital_root(132189)
print(ans)