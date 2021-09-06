
correo = input("Cual es tu correo electronico?: ").strip()

usuario = correo[:correo.index("@")]

dominio = correo[correo.index("@")+1:]

conver = "Su usuario es '{}' y su dominio es '{}'".format(usuario,dominio)

if dominio == 'gmail.com':
 print(conver,' con un dominio popular de Google')

elif dominio == 'Outlook.com':
 print(conver,' con un dominio popular de Microsoft')

elif dominio == 'uabc.com.mx':
 print(conver,' con un dominio popular de la universidad autonoma de Mexico')

else:
    print (conver, ' Es un dominio personalizado')
