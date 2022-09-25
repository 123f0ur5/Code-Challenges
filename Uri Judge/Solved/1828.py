dct = {
    'pedra' : ['papel','Spock'],
    'papel' : ['tesoura', 'lagarto'],
    'tesoura' : ['pedra', 'Spock'],
    'lagarto' : ['pedra', 'tesoura'],
    'Spock' : ['lagarto', 'papel'],
}

n = int(input())

for i in range(n):
    sheldon, raj = input().split()

    if sheldon == raj:
        print(f'Caso #{i+1}: De novo!')
    elif raj in dct[sheldon]:
        print(f'Caso #{i+1}: Raj trapaceou!')
    else:
        print(f'Caso #{i+1}: Bazinga!')