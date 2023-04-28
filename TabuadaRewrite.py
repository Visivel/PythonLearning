n = int(input("Qual numero voce deseja ver ele na tabuada?\n>>> "))
# Pode-se usar tambem "-"*4, igual na linha 6 para ficar mais compacto.
print("+----A tabuada do {}----+".format(n))
for calc in range(11):
    print(">> {} x {} = {}".format(n,calc,n*calc))
print("+{}+".format("-"*22))
