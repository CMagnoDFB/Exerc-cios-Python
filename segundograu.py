print("Vamos resolver um equação de segundo grau no modelo Ax2 + Bx + C=0")
A = int(input("Digite o coeficiente A "))
B = int(input("Digite o coeficiente B "))
C = int(input("Digite o coeficiente C "))

delta = B**2-(4*A*C)

if delta<0:
    print("A equação não possui soluções reais.")
if delta==0:
    print("A equação tem uma solução, e ela é:", -B/2*A)
if delta>0:
    sol1 = (-B+delta)/2*A
    sol2 = (-B-delta)/2*A
    print("A equação tem duas soluções:")
    print("Uma delas é", sol1)
    print("A outra é", sol2)