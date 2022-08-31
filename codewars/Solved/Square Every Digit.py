def square_digits(num):
    num = str(num)
    ans = ''
    for x in num:
        ans += str(int(x)**2)

    return int(ans)

ans = square_digits(9119) #811181
print(ans)