def to_camel_case(text):
    if '-' in text:
        text = text.replace('-','_')
    if '_' in text:
        text = text.split('_')

    print(text)
    
    for i in range(1,len(text)):
        text[i] = text[i][0].upper() + text[i][1:]
    
    return ''.join(text)



ans = to_camel_case("A-Cat_Is_kawaii") # ACatIsKawaii
print(ans)