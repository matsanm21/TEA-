def calcularCalificaión(puntaje):
    if(puntaje >= 0.9 and puntaje <= 1.0):
        calificación = "Sobresaliente"
    elif (puntaje >= 0.8 and puntaje < 0.9):
        calificación = "Notable"
    elif (puntaje >= 0.7 and puntaje < 0.8):
        calificación = "Bien"
    elif (puntaje >= 0.6 and puntaje < 0.7):
        calificación = "Suficiente"
    elif (puntaje >= 0 and puntaje < 0.6): 
        calificación = "Insuficiente"
    else:
        calificación = "Puntaje no válido" 
    return calificación

try: 
    puntaje = float(input("Ingrese la calificaión (0.01 - 1.00): "))
    calificación = calcularCalificaión(puntaje)
    print("El grado de su calificaión es:", calificación)
except: 
    print("Error, debe ingresar un valor numérico")
