def shiftAlfabet(string,step):
    kata = []
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    listString = list(string)
    # print(listString)
    for i in listString:
        if i in alfabet:
            indexAlfa = alfabet.find(i)
            if indexAlfa == len(alfabet) - 1:
                result = 
            kata.append(result)
            # print(result)
        else:
            kata.append(i)
    print("".join(kata))


shiftAlfabet("1234567890a",4)

# a = "ayam"
# b = "y"

# c = a.find(b)
# print(c)



