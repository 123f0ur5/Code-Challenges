import re
from sys import stdin

low = re.compile('[a-z]')
up = re.compile('[A-Z]')
special = re.compile('[\x20-\x2F\x3A-\x40\x5B-\x60\x7B-\x7E]')


while True:
    try:
        s = input()
        valid = True
        if len(s) < 6 or len(s) > 32:
            valid = False
        if low.search(s) == None or up.search(s) == None:
            valid = False
        if special.search(s) != None:
            valid = False
            
        if valid:
            print('Senha valida.')
        else:
            print('Senha invalida.')
    except EOFError:
        break