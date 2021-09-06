texto = input ('Redacta un texto ')

palabra = texto.split()
a=0
while a < len(palabra):
    x=palabra[a]
    if x == 'Fin':
     break
    a+=1
print ('Numero de palabras: ', a)