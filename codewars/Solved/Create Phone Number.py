def create_phone_number(n):
    ans = "({}{}{}) {}{}{}-{}{}{}{}".format(*n) #The * operator unpack the list giving one value for each braces {}
    return ans

ans = create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
print(ans)
