from random import choice
a1 = input("Digite o nome do primeiro aluno(a)\n>>> ")
a2 = input("Digite o nome do segundo aluno(a)\n>>> ")
a3 = input("Digite o nome do terceiro aluno(a)\n>>> ")
print("O aluno sorteado foi: {}".format(choice([a1,a2,a3])))
