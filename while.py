#bucles
#while:se ejecuta mientras sea verdadera

"""i=0

while i <= 15 :
    print(i)
    i +=1
print("ciclo while termino")"""

num = 0
num2 = int(input("ingrese el limite de rango: "))
while num < num2:
    num +=1
    if num % 2 == 0:
        print(num) 