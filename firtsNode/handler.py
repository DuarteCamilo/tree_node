import json

def hello(event, context):
    n = 20

    arbol = []
    estrella = ' ' * (n - 1) + "X"
    arbol.append(estrella)
    for i in range(1, n + 1):
        espacios = ' ' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        arbol.append(espacios + asteriscos)

    cantidad_asteriscos_ultima_fila = 2 * n - 1
    ancho_ultima_fila = cantidad_asteriscos_ultima_fila
    tronco_ancho = ancho_ultima_fila // 3

    if tronco_ancho % 2 == 0:
        tronco_ancho += 1

    for i in range(n // 2):
        espacios = ' ' * ((ancho_ultima_fila - tronco_ancho) // 2)
        asteriscos = '*' * tronco_ancho  
        arbol.append(espacios + asteriscos)
    
    "Arbol al reves"
    arblo2 = []

    cantidad_asteriscos_ultima_fila = 2 * n - 1
    ancho_ultima_fila = cantidad_asteriscos_ultima_fila
    tronco_ancho = ancho_ultima_fila // 3

    if tronco_ancho % 2 == 0:
        tronco_ancho += 1

    for i in range(n // 2):
        espacios = ' ' * ((ancho_ultima_fila - tronco_ancho) // 2)
        asteriscos = '*' * tronco_ancho  
        arblo2.append(espacios + asteriscos)
    
    
    for i in range(n, 0, -1):
        espacios = ' ' * (n - i)
        asteriscos = '*' * (2 * i - 1)
        arblo2.append(espacios + asteriscos)

    
    estrella = ' ' * (n - 1) + "X"
    arblo2.append(estrella)

    response = {
        "body": "\n".join(arbol  + ["\n"] + arblo2) 
        
    }

    return response
