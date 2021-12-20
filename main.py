import random
import Diccionarios.Preguntas as categoria
from Modelos.Participantes import Participante
from BaseDatos.Mongodb import Mongodb
db = Mongodb()
import time

print('\n')
print('     =========================================================================')
print('     Bienvenidos a Quien Quiere Ser millónario el juego que te hace millonario (versión consola PYTHON)')
print('     =========================================================================\n')

participante = None
nombre = None
cedula = None
bolsa = 0
numero_respuesta = 0

x = True
while (x):
    print('     ¿Quisieras volverte millonario, pues ¡participa!\n')
    respuesta = input(
        '     Escribe por consola la letra (y) para participar sino escribe la letra (n) para retirarte: ')
    print('     \n')
    if (respuesta == 'n' or respuesta == 'N'):
        print('     Que lástima pudiste ser uno de nuestros millonarios\n')
        print('     ')
        exit()
    elif (respuesta == 'y' or respuesta == 'Y'):
        print('     De acuerdo, ¡ya estás más cerca de volverte millonario!\n')
        print('     Pero antes necesito que nos regales tus datos, si ya participaste no pueds vovler a concursar: \n')
        nombre = input('     Nombre(s) y Apellido(s): ')
        y = True
        while(y):    
            #try:
                cedula = int(input('     Número de cédula: '))
                print('     \n')
                participante = Participante(nombre, cedula, bolsa, numero_respuesta)
                db.insertar_participante(participante)
                y = False
            #except:
            #   print('     \n')
            #   print('     Ingresaste un número incorrecto vuele a ingresar en número de cedula\n')
            #   continue
        x = False
    else:
        print('     Ocurrió un error, vuelve a responder \n')
        print('     ')



    
print('     Ahora te explicaremos las reglas de juego:')
print('     ------------------------------------------')
time.sleep(1)
print('     Tienes que responder a cada una de nuestras preguntas, por cada una habrán cuatro opciones de respuesta y tendrás que escoger la correcta y solo tendrás una oportunidad. Uuh que tenso. \
Aún así, puedes escoger entre continuar o salir antes de que te presentemos la pregunta. Si llegas a responder correctamente ingresará a tu bolsa de millonario un millón de pesos \
,oiste bien, ¡UN MILLÓN DE PESOS! El cual se multiplicará por el doble cada vez que aciertes. Si decides continuar y erras en la pregunta perderas todo lo que hayas acumulado y saldras \
del juego. Esta oportunidad es única en la vida, nadie se hace millonario de la noche a la mañana, así que ¡aprovéchala! \n')
print("     Será un total de 5 preguntas las que tendrás que responder de manera consecutiva. Recuerda; la primera pregunta tiene valor de 1'000,000 de pesos si la respondes correctamente \
serán ingresados automáticamente en tu bolsa de millonario la pregunta siguiente doblará su valor, en este caso a 2'000,000 de pesos, luego a 4'000,000 de pesos, así hasta lograr los ¡31'000,000 millos de pesos! \
¿No es sorprendente? \n")

x = True
while x:    
    respuesta = input('     Si estás deseo de participar inmediatamente por favor ingresa la letra (y) sino ingresa la letra (n): ')
    print('     \n')
    if (respuesta == 'n' or respuesta == 'N'):
        print('     Es mejor que consultes con la almohada antes de participar\n')
        exit()
    elif (respuesta == 'y' or respuesta == 'Y'):
        print('     ¡Perfecto! Vamos sin mucho preámbulo\n')
        time.sleep(1)
        x = False
    else:
        print('     Ocurrió un error, vuelve a responder \n')
        print('     ')
print('     Pregunta número uno: Geografía \n')
time.sleep(1)

participante = categoria.categorias(1, participante)
time.sleep(1)

if (participante.bolsa == 0):

    db.modificar_participante(participante)
    print('     En este instante te muestro tu registro final \n')
    db.Obtener_participante(participante)
    time.sleep(1)
    answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir   ')
    print('     \n')
    x = True
    while x:
        if (answer_jugador == 'y' or answer_jugador == 'Y'):
            registro = db.collection.find({}).sort("respuesta", -1)
            for reg in registro:
                print(reg)
            print('     \n')
            time.sleep(1)
            print('     De acuerdo. Gracias por participar \n')
            exit()
        elif (answer_jugador == 'n' or answer_jugador == 'N'):
            print('     De acuerdo. Gracias por participar \n')
            exit()
        else:
            answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
            print('     \n')
else:

    print('     ¡Wow! es hora de pasar al siguiente nivel \n')
    time.sleep(1)

answer_jugador = input('  ¿Deseas pasar a la siguiente pregunta confírmanos con la letra (y) o si prefieres retirarte háznolo saber escribiendo la letra (n)? ')
print('     \n')
x = True
while x:
    if (answer_jugador == 'y' or answer_jugador == 'Y'):
        time.sleep(1)
        print('     Pregunta número dos: Entretenimiento \n')
        participante = categoria.categorias(2, participante)
        time.sleep(1)
        x = False
    elif (answer_jugador == 'n' or answer_jugador == 'N'):
        print('     De acuerdo. Gracias por participar \n')
        db.modificar_participante(participante)
        answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir')
        print('     \n')
        x = True
        while x:
            if (answer_jugador == 'y' or answer_jugador == 'Y'):
                registro = db.collection.find({}).sort("respuesta", -1)
                for reg in registro:
                    print(reg)
                print('     \n')
                time.sleep(1)
                print('     De acuerdo. Gracias por participar \n')
                exit()
            elif (answer_jugador == 'n' or answer_jugador == 'N'):
                print('     De acuerdo. Gracias por participar \n')
                exit()
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
            exit()
    else:
        answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
        print('     \n')

if (participante.bolsa == 1000000):

    db.modificar_participante(participante)
    print('     En este instante te muestro tu registro final \n')
    db.Obtener_participante(participante)
    time.sleep(1)
    answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir   ')
    print('     \n')
    x = True
    while x:
        if (answer_jugador == 'y' or answer_jugador == 'Y'):
            registro = db.collection.find({}).sort("respuesta", -1)
            for reg in registro:
                print(reg)
            print('     \n')
            time.sleep(1)
            print('     De acuerdo. Gracias por participar \n')
            exit()
        elif (answer_jugador == 'n' or answer_jugador == 'N'):
            print('     De acuerdo. Gracias por participar \n')
            exit()
        else:
            answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
            print('     \n')
else:

    print('     ¡Wow! es hora de pasar al siguiente nivel \n')
    time.sleep(1)

answer_jugador = input('  ¿Deseas pasar a la siguiente pregunta confírmanos con la letra (y) o si prefieres retirarte háznolo saber escribiendo la letra (n)? ')
print('     \n')
x = True
while x:
    if (answer_jugador == 'y' or answer_jugador == 'Y'):
        time.sleep(1)
        print('     Pregunta número tres: Historia \n')
        participante = categoria.categorias(3, participante)
        time.sleep(1)
        x = False
    elif (answer_jugador == 'n' or answer_jugador == 'N'):
        print('     De acuerdo. Gracias por participar \n')
        db.modificar_participante(participante)
        answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir')
        print('     \n')
        x = True
        while x:
            if (answer_jugador == 'y' or answer_jugador == 'Y'):
                registro = db.collection.find({}).sort("respuesta", -1)
                for reg in registro:
                    print(reg)
                print('     \n')
                time.sleep(1)
                print('     De acuerdo. Gracias por participar \n')
                exit()
            elif (answer_jugador == 'n' or answer_jugador == 'N'):
                print('     De acuerdo. Gracias por participar \n')
                exit()
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
            exit()
    else:
        answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
        print('     \n')

if (participante.bolsa == 2000000):

    db.modificar_participante(participante)
    print('     En este instante te muestro tu registro final \n')
    db.Obtener_participante(participante)
    time.sleep(1)
    answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir   ')
    print('     \n')
    x = True
    while x:
        if (answer_jugador == 'y' or answer_jugador == 'Y'):
            registro = db.collection.find({}).sort("respuesta", -1)
            for reg in registro:
                print(reg)
            print('     \n')
            time.sleep(1)
            print('     De acuerdo. Gracias por participar \n')
            exit()
        elif (answer_jugador == 'n' or answer_jugador == 'N'):
            print('     De acuerdo. Gracias por participar \n')
            exit()
        else:
            answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
            print('     \n')
else:

    print('     ¡Wow! es hora de pasar al siguiente nivel \n')
    time.sleep(1)

answer_jugador = input('  ¿Deseas pasar a la siguiente pregunta confírmanos con la letra (y) o si prefieres retirarte háznolo saber escribiendo la letra (n)? ')
print('     \n')
x = True
while x:
    if (answer_jugador == 'y' or answer_jugador == 'Y'):
        time.sleep(1)
        print('     Pregunta número cuatro: Deportes \n')
        participante = categoria.categorias(4, participante)
        time.sleep(1)
        x = False
    elif (answer_jugador == 'n' or answer_jugador == 'N'):
        print('     De acuerdo. Gracias por participar \n')
        db.modificar_participante(participante)
        answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir')
        print('     \n')
        x = True
        while x:
            if (answer_jugador == 'y' or answer_jugador == 'Y'):
                registro = db.collection.find({}).sort("respuesta", -1)
                for reg in registro:
                    print(reg)
                print('     \n')
                time.sleep(1)
                print('     De acuerdo. Gracias por participar \n')
                exit()
            elif (answer_jugador == 'n' or answer_jugador == 'N'):
                print('     De acuerdo. Gracias por participar \n')
                exit()
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
            exit()
    else:
        answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
        print('     \n')

if (participante.bolsa == 3000000):

    db.modificar_participante(participante)
    print('     En este instante te muestro tu registro final \n')
    db.Obtener_participante(participante)
    time.sleep(1)
    answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir   ')
    print('     \n')
    x = True
    while x:
        if (answer_jugador == 'y' or answer_jugador == 'Y'):
            registro = db.collection.find({}).sort("respuesta", -1)
            for reg in registro:
                print(reg)
            print('     \n')
            time.sleep(1)
            print('     De acuerdo. Gracias por participar \n')
            exit()
        elif (answer_jugador == 'n' or answer_jugador == 'N'):
            print('     De acuerdo. Gracias por participar \n')
            exit()
        else:
            answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
            print('     \n')
else:

    print('     ¡Wow! es hora de pasar al siguiente nivel \n')
    time.sleep(1)

answer_jugador = input('  ¿Deseas pasar a la siguiente pregunta confírmanos con la letra (y) o si prefieres retirarte háznolo saber escribiendo la letra (n)? ')
print('     \n')
x = True
while x:
    if (answer_jugador == 'y' or answer_jugador == 'Y'):
        time.sleep(1)
        print('     Pregunta número cinco: Ciencia \n')
        participante = categoria.categorias(5, participante)
        time.sleep(1)
        x = False
    elif (answer_jugador == 'n' or answer_jugador == 'N'):
        print('     De acuerdo. Gracias por participar \n')
        db.modificar_participante(participante)
        answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir')
        print('     \n')
        x = True
        while x:
            if (answer_jugador == 'y' or answer_jugador == 'Y'):
                registro = db.collection.find({}).sort("respuesta", -1)
                for reg in registro:
                    print(reg)
                print('     \n')
                time.sleep(1)
                print('     De acuerdo. Gracias por participar \n')
                exit()
            elif (answer_jugador == 'n' or answer_jugador == 'N'):
                print('     De acuerdo. Gracias por participar \n')
                exit()
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
            exit()
    else:
        answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
        print('     \n')

if (participante.bolsa == 7000000):

    db.modificar_participante(participante)
    print('     En este instante te muestro tu registro final \n')
    db.Obtener_participante(participante)
    time.sleep(1)
    answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir   ')
    print('     \n')
    x = True
    while x:
        if (answer_jugador == 'y' or answer_jugador == 'Y'):
            registro = db.collection.find({}).sort("respuesta", -1)
            for reg in registro:
                print(reg)
            print('     \n')
            time.sleep(1)
            print('     De acuerdo. Gracias por participar \n')
            exit()
        elif (answer_jugador == 'n' or answer_jugador == 'N'):
            print('     De acuerdo. Gracias por participar \n')
            exit()
        else:
            answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
            print('     \n')
else:

    print(' CONGRATULATIONS! Has de volverte millonario que dicha por ti \n')
    time.sleep(1)
    db.modificar_participante(participante)
    print('     En este instante te muestro tu registro final \n')
    db.Obtener_participante(participante)
    time.sleep(1)
    answer_jugador = input('  Puedes consultar el registro de participantes si lo deaseas, escribe la letra (y) para mirar la tabla de participantes sino escribe la letra (n) para salir   ')
    print('     \n')
    x = True
    while x:
        if (answer_jugador == 'y' or answer_jugador == 'Y'):
            registro = db.collection.find({}).sort("respuesta", -1)
            for reg in registro:
                print(reg)
            print('     \n')
            time.sleep(1)
            print('     De acuerdo. Gracias por participar \n')
            exit()
        elif (answer_jugador == 'n' or answer_jugador == 'N'):
            print('     De acuerdo. Gracias por participar \n')
            exit()
        else:
            answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
            print('     \n')
    exit()

















