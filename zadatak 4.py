def unazad_Fun(x):
    return x[::-1]

input1 = input("Unesi neki string ")
input2 = input("Unesi jos neki string ")

mojTxt = unazad_Fun(str(input1) + ' ' + str(input2))
print(mojTxt.title())
