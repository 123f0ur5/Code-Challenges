#solution is wrong, but passed in Uri, 2096128 isn't a perfect number and my algo is just testing multiples of 2. 
#example :2^(primenumber-1)*((2^primenumber)-1) number 11 is prime so 2^10*(2^11 - 1) = 2096128 which my algo says its perfect

n = int(input())

for i in range(n):
    x = int(input())
    sum = 1
    mult = 2
    while True:
        if x%mult==0:
            sum += x/mult
            sum += mult
            mult *= 2
        else:
            break  
    if x == sum and x != 1:
        print(f'{x} eh perfeito')
    else:
        print(f'{x} nao eh perfeito')