def reverse_string(str):
    result = ""
    #obhojda stringa i dobavq tekushtiqt simvol otpred
    for i in str:
        result = i + result
    return result

def reverse_string_rec(str):
    #proverqva dali str e prazen
    if str == "":
        return str
    return reverse_string_rec(str[1:]) + str[0]

str = "Beroe"
print(reverse_string(str))
print(reverse_string_rec(str))