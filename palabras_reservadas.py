""" Las palabras reservadas, son palabras exclusivas del
lenguaje de programacion Python, que tienen un significado especial
y no pueden ser utilizadas como identifcadores, funciones
 """

#Lista de palabras reservadas
palabras_reservadas = [
    'False',
    'None',
    'True',
    'and',
    'as',
    'assert',
    'break',
    'class',
    'continue',
    'def',
    'del',
    'elif',
    'else',
    'except',
    'finally',
    'for',
    'from',
    'global',
    'if',
    'import',
    'in',
    'is',
    'lambda',
    'nonlocal',
    'not',
    'or',
    'pass',
    'raise',
    'return',
    'try',
    'while',
    'with',
    'yield'
]

#Las palabras reservadas no deben de usar . Ejemplo

nombre = "Antonio"
print (nombre)

# Concatenacion
nombre_completo = nombre + " " + "Luciano"
print(nombre_completo)

#Obtener el total de palabras reservadas 
print(len(palabras_reservadas))

#esto no se debe hacer

#class = "programacion estructurada" 
#print (nombre)
#print (class)