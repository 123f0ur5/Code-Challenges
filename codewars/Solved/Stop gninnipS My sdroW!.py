def spin_words(sentence):
    list = sentence.split()
    for i in range(0,len(list)):
        if(len(list[i]) >= 5):
            palavra =''.join(reversed(list[i]))
            list[i] = palavra
    return list


palavra = str(input())

teste = spin_words(palavra)
teste = ' '.join(teste)

print(teste)