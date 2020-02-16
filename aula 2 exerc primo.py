
loopar=True
continuar=True
divisor=2
while loopar:
    n = int(input("Digite um número para verificar se ele é primo: "))
    if n==1 or n==2:
        print("Seu número é primo.")
             
        
    
    while divisor<n and continuar:
        if n%divisor==0:
            print("Seu número não é primo.")
            continuar=False

        elif divisor<n: 
            print("Seu número é primo.") 
            continuar=False
        else:
            divisor+=1
    continuar=True
           
