Lst = [] 
maxLengthList = int(input("NO of inputs : "))
while len(Lst) < maxLengthList:
    item = input("Enter your Item to the List: ")
    Lst.append(item)
    print(Lst)
print("That's your List")
print(Lst)


def Convert(Lst):
    conv = {Lst[i]: Lst[i + 1] for i in range(0, len(Lst), 2)}
    return conv
print("Your converted List to Dictionary is : ")
print(Convert(Lst))