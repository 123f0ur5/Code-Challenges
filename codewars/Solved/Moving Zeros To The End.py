def move_zeros(lst):
    lst = list(lst)
    for x in range(len(lst)):
        if lst[x] == 0:
            lst.remove(0)
            lst.append(0)

    return lst


ans = move_zeros([9, 0, 9, 1, 2, 1, 1, 3, 1, 9, 0, 0, 9, 0, 0, 0, 0, 0, 0, 0])
print(ans)