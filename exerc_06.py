#Veficar os numeros pares em impares entre um numero
par = 0
impar = 0
x = int(input("Digite o primeiro numero: "))
y = int(input("Digite o segundo número: "))

for i in range(x+1,y):
    v = i%2
    if (v == 0):
        print(f"{i} é Par")
        par = par + 1
        

    else:
        print(f"{i} é impar") 
        impar = impar + 1
        

print(f"contem {par} numeros pares e {impar} numeros impares")

     





