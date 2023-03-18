#bucles
#while:se ejecuta mientras sea verdadera

"""i=0

while i <= 15 :
    print(i)
    i +=1
print("ciclo while termino")

num = 0
num2 = int(input("ingrese el limite de rango: "))
while num < num2:
    num +=1
    if num % 2 == 0:
        print(num) """
        

#programa que solicite confirmar contraseña 

contraseña = input("ingrese una contraseña: ")

confirmacion = input("ingrese la clave de confirmacion: ")

while contraseña != confirmacion :
    print("su contraeña es incorrecta ingrese de nuevo")
    contraseña = input("ingrese una contraseña: ")
    confirmacion = input("ingrese la clave de confirmacion: ")
print("validacion confirmada")

    