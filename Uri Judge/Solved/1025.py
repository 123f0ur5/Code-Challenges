def search(lst, q):
    tamanho_lista = len(lst)
    inicio = 0
    fim = tamanho_lista-1

    while inicio <= fim:
        meio = (inicio + fim)//2
        if lst[meio] == q:
            while True:
                if lst[meio-1] == q:
                    meio -= 1
                else:
                    break
            return meio + 1
        elif lst[meio] < q:
            inicio = meio + 1
        elif lst[meio] > q:
            fim = meio -1
    
    return False

case_num = 0
while True:
    case = True
    n, q = map(int, input().split())
    if n == q == 0:
        break
    ans = [[] for _ in range(q)]
    lst = []
    for i in range(n):
        x = int(input())
        lst.append(x)
    
    lst.sort()

    for i in range(q):
        x = int(input())
        result = search(lst,x)
        if result:
            ans[i].append(x)
            ans[i].append(f' found at {result}')
        else:
            ans[i].append(x)
            ans[i].append(' not found')
    case_num += 1
    for i in range(q):
        if case:
            print(f'CASE# {case_num}:')
            case = False
        
        print(f'{ans[i][0]}{ans[i][1]}')