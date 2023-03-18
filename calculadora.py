import math
operaciones = ""

print("escoja la operaciones escriba el nombre de la operacion")
print("suma")
print("resta")
print("multiplicaion")
print("division")
print("potencia")
print("raiz")
print("cambiar numeros")
print("salir")
num1=int(input("ingrese el primer numero:"))
num2=int(input("ingrese el segundo numero:"))



while operaciones != "salir":    
    operaciones = input("escoja una operacion a realizar: ")
    
    if operaciones == "suma":
        print(f"la sumade {num1} + {num2} = {num1+num2}")
    elif operaciones == "resta":
        print(f"la resta de {num1} - {num2} = {num1-num2}")
    elif operaciones == "multiplicacion":
        print(f"la multiplicacion de {num1} * {num2} = {num1*num2}")
    elif operaciones == "division":
        print("el 0 no puede ser divisor")
        while num2 ==0:      
            num2 = int(input("ingrese el nuevo numero a cambiar: ")) 
        print(f"la resta de {num1} / {num2} = {num1/num2}")
    elif operaciones == "potencia":
        print(f"la resta de {num1} ^ {num2} = {math.pow(num1,num2)}")
    elif operaciones == "raiz":
        if num1 and num2 < 0:
            print("no pueen ser numeros negativos")
            num1 = int(input("ingrese el nuevo numero a cambiar: "))
            num2 = int(input("ingrese el nuevo numero a cambiar: "))
        elif num1 < 0:
            print("no puede ser negativos")
            num1 = int(input("ingrese el nuevo numero a cambiar: "))
        elif num2 < 0:
            print("no puede ser negativos")
            num2 = int(input("ingrese el nuevo numero a cambiar: "))
        else:
            print(f"la raiz de {num1} = {math.sqrt(num1)}")
            print(f"la raiz de {num2} = {math.sqrt(num2)}")
    elif operaciones == "cambiar numeros" :
        num1=int(input("ingrese el primer numero:"))
        num2=int(input("ingrese el segundo numero:"))
    elif operaciones == "salir":
        print("se salio de la calculadora")
    else:
        print("opcion no encontrada")
        