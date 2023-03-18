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
        print(num) 
        

#programa que solicite confirmar contraseña 

contraseña = input("ingrese una contraseña: ")

confirmacion = input("ingrese la clave de confirmacion: ")

while contraseña != confirmacion :
    print("su contraeña es incorrecta ingrese de nuevo")
    contraseña = input("ingrese una contraseña: ")
    confirmacion = input("ingrese la clave de confirmacion: ")
print("validacion confirmada") """


#hacer un programa donde el usuario escoja entre varios lenguajes de programacion (HTML, CSS , JAVASCRIPT, PYTHON) y segun la opcion escogida muestre para que sirve. debe tener una opcion pra salir

print("escoja su lenguaje de programacion")
print("1.HTML")
print("2.CSS")
print("3.JAVASCRIPT")
print("4.PYTHON")
print("5.salir")

lenguaje = ""

"""while lenguaje != 5 :
    lenguaje = int(input("escoja una opcion: "))
    if lenguaje == 1:
        print("HTML es un lenguaje de Hipertexto esto es lo que vera los usuarios")
    elif lenguaje == 2:
        print("CSS es un lengauje de estilo este sirve para darle estilo Al HTML")
    elif lenguaje == 3:
        print("JAVASCRIPT es un lenguaje de programacion este sirve para darle funcionalidad al HTML")
    elif lenguaje == 4:
        print("PYTHON es un lenguaje de programacion este sirve para darle funcionalidad al HTML")
    elif lenguaje == 5:
        print("acaba de salir")"""

while lenguaje != "salir" :
    lenguaje = input("escoja una opcion: ")
    if lenguaje == "html":
        print("HTML es un lenguaje de Hipertexto esto es lo que vera los usuarios")
    elif lenguaje == "css":
        print("CSS es un lengauje de estilo este sirve para darle estilo Al HTML")
    elif lenguaje == "javascript":
        print("JAVASCRIPT es un lenguaje de programacion este sirve para darle funcionalidad al HTML")
    elif lenguaje == 4:
        print("PYTHON es un lenguaje de programacion este sirve para darle funcionalidad al HTML")
    elif lenguaje == "salir":
        print("acaba de salir")
    else :
        print("lenguaje no encontrado")

    