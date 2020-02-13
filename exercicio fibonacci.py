n = int(input("Quantos números da sequência de Fibonacci você deseja? "))
n1 = 0
n2 = 1
n3 = n2 + n1
n4 = n3 + n2
n5 = n4 + n3
n6 = n5 + n4

if n==0:
    print("Nenhum número então.")
if n==1:
    print(n1)
if n==2:
    print(n1, n2)
if n==3:
    print(n1, n2, n3)
if n==4:
    print(n1, n2, n3, n4)
if n==5:
    print(n1, n2, n3, n4, n5)
if n==6:
    print(n1, n2, n3, n4, n5, n6)