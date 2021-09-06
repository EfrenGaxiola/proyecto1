
import numpy as np
import time

condiciones ={'piedra': 'tijera', 'tijera': 'papel', 'papel': 'piedra'}

player = input('Introduce tu eleccion: piedra, papel, tijera: ')
while player not in {'piedra', 'papel', 'papel'}:
    print("Introdujiste algo erroneo")
    player = input('Introduce tu eleccion: piedra, papel, tijera: ')
PC = np.random.choice(['piedra', 'tijera', 'papel'])

time.sleep(1)
print("Has seleccionado: ",player)
print("La IA ha seleccionado: ",PC)
time.sleep(1.5)

if condiciones[player] == PC:
    print('¡Eres el numero 1!')
elif condiciones[PC] == player:
    print('Perdedor, eres un perdedor')
else:
    print('¡Empataron, es increible!')

