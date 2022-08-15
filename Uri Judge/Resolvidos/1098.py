i = 0
j = 1

for x in range(0,11):
    for y in range(0,3):
        if(x == 0 or x == 5 or x == 10):
            print("I={:.0f} J={:.0f}".format(i,j))
        else:
            print("I={:.1f} J={:.1f}".format(i,j))
        j += 1
    j -= 2.8
    i += 0.2