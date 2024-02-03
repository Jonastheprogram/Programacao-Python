x = int(input("Informe o inicio da contagem: "))
y = int(input("Informe o fim da contagem: "))

if x > y:
    print("o fim da contagem não pode ser maior que o inicio da contagem")
for i in range(x+1,y,1):
    print(i)
    #codigo para contar numeros entre dois números inteiros