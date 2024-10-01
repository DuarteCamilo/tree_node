n = 18

estrella1 = ' ' * (n - 1) 
estrella2 ="X"
print(estrella1 + estrella2)
for i in range(1, n + 1):
    espacios = ' ' * (n - i)
    asteriscos = '*' * (2 * i - 1)
    print(espacios + asteriscos)

cantidad_asteriscos_ultima_fila = 2 * n - 1

ancho_ultima_fila = cantidad_asteriscos_ultima_fila
tronco_ancho = ancho_ultima_fila // 3

print(ancho_ultima_fila)

if tronco_ancho % 2 == 0:
    tronco_ancho += 1

for i in range(n//2):
    espacios = ' ' * ((ancho_ultima_fila - tronco_ancho) // 2)
    asteriscos = '*' * tronco_ancho  
    print(espacios + asteriscos)  