num = int(input("Qual numero voce deseja calcular?\n>>> "))
metodo = int(input("Qual metodo?\n(1) Soma\n(2) Subtracao\n(3) Divisao\n(4) Multiplicação\n(Use 1,2,3,4 para responder)\n>>> "))
calc = int(input("Qual numero vai usar para calcular?\n(Qual vai mulplicar, somar etc)\n>>> "))
if metodo==1:
    print("A soma de {} com {} é:\n[{}]".format(num,calc,num+calc))
else:
    if metodo==2:
        print("A subtracao de {} com {} é:\n[{}]".format(num,calc,num-calc))
    else:
        if metodo==3:
            print("A divisao de {} com {} é:\n[{}]".format(num,calc,round(num/calc,3)))
            # Usei round pq acho que nos outros so vai Float caso for proposital
            # Tipo caso a pessoa coloque 0.444 no "num", ai ele vai ficar locao msm.
        else:
            if metodo==4:
                print("A multiplicação de {} com {} é:\n[{}]".format(num,calc,num*calc))
