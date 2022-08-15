def is_pangram(s):
    remo_table = dict.fromkeys(map(ord, '.,!?:123456789'))
    s = str(s).translate(remo_table)
    s = s.replace(' ', '')
    s = s.upper()

    pangram = set()
    for x in s:
        if not x in pangram:
            pangram.add(x)
    return len(pangram) == 26



a = str(input())
print(is_pangram(a))