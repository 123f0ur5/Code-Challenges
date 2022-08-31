import re

def order(sentence):
    sentence = sentence.split()
    new_sentence = ['' for _ in range(len(sentence))]
  
    for x in sentence:
        new_sentence [int(re.sub('\D',"",x))-1] = x

    return ' '.join(new_sentence)

ans = order('4of Fo1r pe6ople g3ood th5e the2')
print(ans)