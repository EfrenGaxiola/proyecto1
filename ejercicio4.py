import re

def validacion(palabra):
    validar = '^[a-zA-Z]'

    return bool(re.search(validar, palabra))
while True:
          
        nombre = input('Introduce el nombre completo ')
        print(validacion(nombre))
        if validacion(nombre) == True:
         break
         
    
def validacion2(palabra2):
    validar2 = '^[a-zA-Z0-9]'

    return bool(re.search(validar2, palabra2))
while True:    
        fecha = input('Introduce fecha de cumpleaños ')
        print(validacion2(fecha))
        if validacion2(fecha) == True:
         break

def validacion3(palabra3):
    validar3 = '^[a-zA-Z,]'

    return bool(re.search(validar3, palabra3))
while True:    
        vivienda = input('Introduce donde vives ')
        print(validacion3(vivienda))
        if validacion3(vivienda) == True:
         break

while True:
    try:
        edad = int(input('Introduce tu edad '))
        break
    except ValueError:
        print('Solo numeros')

print ('Nombre: ',nombre)
print ('Fecha de cumpleaños:', fecha )
print ('Lugar donde vive: ', vivienda)
print ('Edad: ', edad)