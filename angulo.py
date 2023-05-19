import math as mt
ang1 = float(input("Digite um angulo\n>>> "))
print("O seno de {:.0f} sera {:.3f}".format(ang1,mt.sin(mt.radians(ang1))))
print("O cosseno de {:.0f} sera {:.3f}".format(ang1,mt.cos(mt.radians(ang1))))
print("A tangente de {:.0f} sera {:.3f}".format(ang1,mt.tan(mt.radians(ang1))))
# Sim eu sei que eu podia ter colocado from math import, mas fds
