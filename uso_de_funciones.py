#uso de funciones en python
# 1.- función que salude
# 2.- función que recibe 2 argumentos y hace una opción matematica

def saludar():
    print("Hola, este es un saludo")

    saludar()

# Ejercicio 2
def suma(numero_uno,numero_dos):
    suma = numero_uno + numero_dos
    print(suma)

    suma(10,5)

#ejercicio 3 - Pedir al usuario dos numeros y pasarlos como argumentos y realizar unasuma

x = input('Inserta un número:')
y = input('Inserta otro número:')
xx = int(x)
yy = int(y)
sum = xx + yy
print(sum)
