contador = 0
suma = 0 
while True: 
    numero = input("Ingrese un número: ")
    if (numero == "salir"):
        break 
    contador = contador + 1
    suma = suma + int(numero)
print("Contador", contador)
print("Suma", suma)
print("Promedio", suma/contador)
