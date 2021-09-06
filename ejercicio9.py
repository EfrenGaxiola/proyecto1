subtotal = int(input("Cuanto a pagar? "))
propina = float(input ('La propina es 18%, 20%, 25%'))

print ('El total maximo de personas son 4')
personas = int(input('Cuantas personas son?'))
while personas >4:
    print ('No es posible atender a esas personas')
    personas = int(input('Cuantas personas son?'))
if personas == 4:
    Total = subtotal + (subtotal * propina)
    print ('El Total a pagar es: $',Total,'\nCada persona pagara un porcentaje')
    persona1= float(input('Yo pagare el: '))
    por1 = Total * persona1
    persona2= float(input('Yo pagare el: '))
    por2 = Total * persona2
    persona3= float(input('Yo pagare el: '))
    por3 = Total * persona3
    persona4= float(input('Yo pagare el: '))
    por4 = Total * persona4
    print ('El total a pagar es: $',Total ,'\nLa persona 1 pago el: ', persona1*100,'%', ' o $',por1, '\nLa persona 2 pago el: ', persona2*100, '%',' o $',por2, '\nLa persona 3 pago el: ', persona3*100, '%',' o $',por3, '\nLa persona 4 pago el: ', persona4*100, '%',' o $',por4  )
elif personas == 3:
    Total = subtotal + (subtotal * propina)
    print ('El Total a pagar es: $',Total,'\nCada persona pagara un porcentaje')
    persona1= float(input('Yo pagare el: '))
    por1 = Total * persona1
    persona2= float(input('Yo pagare el: '))
    por2 = Total * persona2
    persona3= float(input('Yo pagare el: '))
    por3 = Total * persona3
    print ('El total a pagar es: $',Total ,'\nLa persona 1 pago el: ', persona1*100,'%', ' o $',por1, '\nLa persona 2 pago el: ', persona2*100, '%',' o $',por2, '\nLa persona 3 pago el: ', persona3*100, '%',' o $',por3)
elif personas == 2:
    Total = subtotal + (subtotal * propina)
    print ('El Total a pagar es: $',Total,'\nCada persona pagara un porcentaje')
    persona1= float(input('Yo pagare el: '))
    por1 = Total * persona1
    persona2= float(input('Yo pagare el: '))
    por2 = Total * persona2
    print ('El total a pagar es: $',Total ,'\nLa persona 1 pago el: ', persona1*100,'%', ' o $',por1, '\nLa persona 2 pago el: ', persona2*100, '%',' o $',por2)
else:
    Total = subtotal + (subtotal * propina)
    print ('Al ser una unica persona, solo de dara el total a pagar')
    print ('El total a pagar es: $',Total)  