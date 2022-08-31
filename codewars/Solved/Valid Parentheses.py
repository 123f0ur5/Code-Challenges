def valid_parentheses(string):
    count = 0
    if string.count('(') != string.count(')'):
        return False
    
    for p in string:
        if p == '(':
            count += 1
        elif p == ')':
            count -= 1
            
        if count < 0:
            return False
    
    return True

ans = valid_parentheses("()))))((((")
print(ans)