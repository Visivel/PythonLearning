# Primeiro programa que eu uso import xd
import random
chance = int(input("Digite um valor que deseja tirar na sorte de 1 a 16.\n>>> "))
valor = random.randint(1,16)
if chance >16:
    print("Desculpe, apenas numeros de 1 a 16.")
else:
    if chance == valor:
        print("Que sorte!")
    else:
        print("Que azar")
