def bouncing_ball(h, bounce, window):
    cont = 0
    if h <= 0:
        return -1
    elif bounce <= 0 or bounce >= 1:
        return -1
    elif window > h:
        return -1
    while h > window:
        cont += 1
        h = h * bounce
    
    return cont*2-1

print(bouncing_ball(30, 1, 1.5))
