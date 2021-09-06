import random
import re
num = random.randrange(1,5)
adivinador = int(input('Adivina un numero entre 1 y 50: '))
derrotas = 0

while adivinador >5:
    print ('El numero no esta en el rango')
    adivinador = int(input('Adivina un numero entre 1 y 50: '))
while adivinador != num: 
 def validacion2(palabra2):
     validar2 = '^[Si]'

     return bool(re.search(validar2, palabra2))
 while True:    
        decision = input('Quiere seguir jugando? Si o No ')        
        if decision == "Si":      
         while adivinador >5:
          print ('El numero no esta en el rango')
         adivinador = int(input('Adivina un numero entre 1 y 50: '))
        dorrotas = derrotas + 1
        while adivinador == num:
         print ('Felicidades has atinado el numero que esto pensando','\n' 'Numnero de derrotas: ',derrotas)
         break
         #print(validacion2(adivinador))
        if validacion2(decision) == False:
            print('Gracias por jugar')
            break   
 

 
    

