try:
    entrada = input("Ingrese el nombre del archivo: ")
    archivo = open(entrada, "r")
    for linea in archivo:
        print(linea.upper())
except:
    print("Error, no existe el archivo")
