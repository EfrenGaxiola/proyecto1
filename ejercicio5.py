def acro(conver):

    contador = conver[0]

    for x in range(1, len(conver)):
        if conver[x-1] == ' ':

            contador += conver[x]

    contador = contador.upper()

    return contador

palabra = input('Ingresa el texto')

print(acro(palabra))


