#Getting Runtime error because it take so much time to calculate 2bil
def divide(dividend, divisor):
    cont = 0
    if dividend > pow(2,31) or dividend < -abs(pow(2,31)):
        return -1
    elif divisor < 0 and dividend < 0:
        while abs(dividend) >= abs(divisor):
            dividend = abs(dividend) - abs(divisor)
            cont += 1
            print(cont, dividend)
        return cont
    elif divisor < 0 or dividend < 0:
        while abs(dividend) >= abs(divisor):
            dividend = abs(dividend) - abs(divisor)
            cont += 1
        return -abs(cont)
    else:
        while dividend >= divisor:
            dividend -= divisor
            cont += 1
        return cont


print(divide(-2147483648, -5000))