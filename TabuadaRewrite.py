n = int(input("Qual numero voce deseja ver ele na tabuada?\n>>> "))
n2 = int(input("Ate onde voce quer que a tabuada va?\n>>> "))
print("+----A tabuada do {}----+".format(n))
for calc in range(n2+1):
    print(">> {} x {} = {}".format(n,calc,n*calc))
print("+{}+".format("-"*22))
