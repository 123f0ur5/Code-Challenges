def email(replacements):

    for key in replacements.keys():
        if len(replacements[key]) == 0:
            return False


    return True
    

dct = {
    'first_name': ''
}
print(email(dct))