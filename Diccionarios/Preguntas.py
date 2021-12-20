import random
from BaseDatos import Mongodb
import time

def categorias(nivel, participante):
    
    valor = {
        1: 1000000,
        2: 2000000,
        3: 4000000,
        4: 8000000,
        5: 16000000
    }

    if nivel == 1: #Geografía
        categoria_uno = {
            1: '¿Cuál es el idioma más hablado en Suiza?',
            2: '¿Qué país está entre Perú y Colombia?',
            3: '¿Cuál es el río más largo de Europa Occidental?',
            4: '¿Qué lago baña la ciudad de Ginebra?',
            5: '¿Cuál es la capital de Indonesia?'
        }
        respuestas_uno = [['Alemán','Español','Inglés','Filandés'],
                        ['Venezuela','Bolivia','Argentina','Ecuador'],
                        ['Nilo','Danubio','Rin','Volga'],
                        ['Leman', 'Bolsena', 'Iseo','Trasimeno'],
                        ['Laos','Viena','Torino','Jakarta']]
        respuestas_uno_correcta = ['Alemán','Ecuador','Rin','Leman','Jakarta']

        pregunta = None
        correcta = None
        i = random.randrange(1,5)

        for key, value in categoria_uno.items():
            if i == key:
                pregunta = value
                correcta = respuestas_uno_correcta[i-1]
        answer = respuestas_uno[i-1]
        answer = random.sample(answer, len(answer))

        print(f'     {pregunta} \n')
        print(f'     A. {answer[0]}     B. {answer[1]}')
        print(f'     C. {answer[2]}     D. {answer[3]} \n')
        answer_jugador = input('      Ingresa por favor la letra que corresponda a tu respuesta: ')
        print('     \n')

        x = True
        while x:
            if (answer_jugador == 'a' or answer_jugador == 'A'):
                answer_jugador = 0
                x = False
            elif (answer_jugador == 'b' or answer_jugador == 'B'):
                answer_jugador = 1
                x = False
            elif (answer_jugador == 'c' or answer_jugador == 'C'):
                answer_jugador = 2
                x = False
            elif (answer_jugador == 'd' or answer_jugador == 'D'):
                answer_jugador = 3
                x = False
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
        for ans in answer:
            if (ans == answer[answer_jugador]):
                if(answer[answer_jugador] == correcta):
                    print(f'     ¡Muy bien! Acabas de ganar {valor[nivel]} \n')
                    if participante.bolsa == 0:
                        for key, value in valor.items():
                            if key == nivel:
                                participante.bolsa = value
                                participante.numero_respuesta = nivel
                                return participante
                    else:
                            for key, value in valor.items():
                                if key == nivel:
                                    participante.bolsa = value + participante.bolsa
                                    participante.numero_respuesta = nivel
                                    return participante

                else:
                        participante.bolsa = 0
                        participante.numero_respuesta = nivel
                        time.sleep(1)
                        print('     Ah tu respuesta ha sido incorrecta, que mal acabas de perder la opotunidad de tu vida. \n')
                        print('     GAME OVER \n')
                        return participante

    elif nivel == 2: #Entretenimiento
        categoria_uno = {
            1: '¿Cuál es el oso más famoso del parque nacional de Yellowstone?',
            2: '¿Qué actor, que no era el feo ni el malo, era el bueno?',
            3: '¿Con qué director de cine italiano se casó la actriz Giulietta Masina?',
            4: '¿Quién fue la gran ganadora de los Grammy Latinos 2018?',
            5: '¿Cuál de los Siete Enanitos no tenía barba?'
        }
        respuestas_uno = [['Mogui','Winnie pooh','Barney','Yogui'],
                        ['Brad Pitt','Clint Eastwood','Leonardo Dicaprio','Jason Momoa'],
                        ['Gabriel Marquez','Luchino Visconti','Federico Fellini','Pier Pasolini'],
                        ['Rosalia','Shakira','Becky G','Paulina Rubio'],
                        ['Guillo', 'Bolsena', 'Mudito','Gruñon']]
        respuestas_uno_correcta = ['Yogui','Clint Eastwood','Federico Fellini','Rosalia','Mudito']

        pregunta = None
        correcta = None
        i = random.randrange(1,5)

        for key, value in categoria_uno.items():
            if i == key:
                pregunta = value
                correcta = respuestas_uno_correcta[i-1]
        answer = respuestas_uno[i-1]
        answer = random.sample(answer, len(answer))

        print(f'     {pregunta} \n')
        print(f'     A. {answer[0]}     B. {answer[1]}')
        print(f'     C. {answer[2]}     D. {answer[3]} \n')
        answer_jugador = input('      Ingresa por favor la letra que corresponda a tu respuesta: ')
        print('     \n')

        x = True
        while x:
            if (answer_jugador == 'a' or answer_jugador == 'A'):
                answer_jugador = 0
                x = False
            elif (answer_jugador == 'b' or answer_jugador == 'B'):
                answer_jugador = 1
                x = False
            elif (answer_jugador == 'c' or answer_jugador == 'C'):
                answer_jugador = 2
                x = False
            elif (answer_jugador == 'd' or answer_jugador == 'D'):
                answer_jugador = 3
                x = False
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
        for ans in answer:
            if (ans == answer[answer_jugador]):
                if(answer[answer_jugador] == correcta):
                    print(f'     ¡Muy bien! Acabas de ganar {valor[nivel]} \n')
                    if participante.bolsa == 0:
                        for key, value in valor.items():
                            if key == nivel:
                                participante.bolsa = value
                                participante.numero_respuesta = nivel
                                return participante
                    else:
                            for key, value in valor.items():
                                if key == nivel:
                                    participante.bolsa = value + participante.bolsa
                                    participante.numero_respuesta = nivel
                                    return participante
                else:
                        participante.bolsa = 0
                        participante.numero_respuesta = nivel
                        time.sleep(1)
                        print('     Ah tu respuesta ha sido incorrecta, que mal acabas de perder la opotunidad de tu vida. \n')
                        print('     GAME OVER \n')
                        return participante

    elif nivel == 3: #Historia
        categoria_uno = {
            1: '¿Qué reina británica era hija de los Reyes Católicos?',
            2: '¿Qué país fue llamado la Galia por los romanos?',
            3: '¿Qué batalla crucial tuvo lugar en 1815?',
            4: '¿Cuál era la ciudad hogar de Marco Polo?',
            5: '¿Quién era el emperador de Roma cuando murió Jesús?'
        }
        respuestas_uno = [['Catalina de Aragón','Catalina la grande','Julieta','Cleopatra'],
                        ['Francia','Italia','Inglaterra','España'],
                        ['Té','Opio','Waterloo','Boston'],
                        ['Venecia','Torino','Bologña','Turin'],
                        ['Julio Cesar', 'Alejandro', 'Artemio','Tiberio']]
        respuestas_uno_correcta = ['Catalina de Aragón','Francia','Waterloo','Venecia','Tiberio']
        pregunta = None
        correcta = None
        i = random.randrange(1,5)

        for key, value in categoria_uno.items():
            if i == key:
                pregunta = value
                correcta = respuestas_uno_correcta[i-1]
        answer = respuestas_uno[i-1]
        answer = random.sample(answer, len(answer))

        print(f'     {pregunta} \n')
        print(f'     A. {answer[0]}     B. {answer[1]}')
        print(f'     C. {answer[2]}     D. {answer[3]} \n')
        answer_jugador = input('      Ingresa por favor la letra que corresponda a tu respuesta: ')
        print('     \n')

        x = True
        while x:
            if (answer_jugador == 'a' or answer_jugador == 'A'):
                answer_jugador = 0
                x = False
            elif (answer_jugador == 'b' or answer_jugador == 'B'):
                answer_jugador = 1
                x = False
            elif (answer_jugador == 'c' or answer_jugador == 'C'):
                answer_jugador = 2
                x = False
            elif (answer_jugador == 'd' or answer_jugador == 'D'):
                answer_jugador = 3
                x = False
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
        for ans in answer:
            if (ans == answer[answer_jugador]):
                if(answer[answer_jugador] == correcta):
                    print(f'     ¡Muy bien! Acabas de ganar {valor[nivel]} \n')
                    if participante.bolsa == 0:
                        for key, value in valor.items():
                            if key == nivel:
                                participante.bolsa = value
                                participante.numero_respuesta = nivel
                                return participante
                    else:
                            for key, value in valor.items():
                                if key == nivel:
                                    participante.bolsa = value + participante.bolsa
                                    participante.numero_respuesta = nivel
                                    return participante
                else:
                        participante.bolsa = 0
                        participante.numero_respuesta = nivel
                        time.sleep(1)
                        print('     Ah tu respuesta ha sido incorrecta, que mal acabas de perder la opotunidad de tu vida. \n')
                        print('     GAME OVER \n')
                        return participante
    elif nivel == 4: #Deportes
        categoria_uno = {
            1: '¿Qué pieza de ajedrez puede hacer un movimiento en forma de L??',
            2: '¿Cómo se llaman los deportistas que practican el judo?',
            3: '¿Qué deporte practican los Harlem Globetrotters?',
            4: '¿A cuántos puntos se disputa un set en el tenis de mesa?',
            5: '¿Qué obtienes si añades fruta fresca al vino tinto?'
        }
        respuestas_uno = [['Torre','Peón','Alfíl','Caballo'],
                        ['Judistas','Judokas','Judenses','judos'],
                        ['Baloncesto','Fútbol','Americano','Ciclismo'],
                        ['Veintiuno','Ventidos','Veinte','Dicinueve'],
                        ['Cubalibre', 'Sangría', 'Verano','Cabeza de jabalí']]
        respuestas_uno_correcta = ['Caballo','Judokas','Baloncesto','Veintiuno','Sangría']
        pregunta = None
        correcta = None
        i = random.randrange(1,5)

        for key, value in categoria_uno.items():
            if i == key:
                pregunta = value
                correcta = respuestas_uno_correcta[i-1]
        answer = respuestas_uno[i-1]
        answer = random.sample(answer, len(answer))

        print(f'     {pregunta} \n')
        print(f'     A. {answer[0]}     B. {answer[1]}')
        print(f'     C. {answer[2]}     D. {answer[3]} \n')
        answer_jugador = input('      Ingresa por favor la letra que corresponda a tu respuesta: ')
        print('     \n')

        x = True
        while x:
            if (answer_jugador == 'a' or answer_jugador == 'A'):
                answer_jugador = 0
                x = False
            elif (answer_jugador == 'b' or answer_jugador == 'B'):
                answer_jugador = 1
                x = False
            elif (answer_jugador == 'c' or answer_jugador == 'C'):
                answer_jugador = 2
                x = False
            elif (answer_jugador == 'd' or answer_jugador == 'D'):
                answer_jugador = 3
                x = False
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
        for ans in answer:
            if (ans == answer[answer_jugador]):
                if(answer[answer_jugador] == correcta):
                    print(f'     ¡Muy bien! Acabas de ganar {valor[nivel]} \n')
                    if participante.bolsa == 0:
                        for key, value in valor.items():
                            if key == nivel:
                                participante.bolsa = value
                                participante.numero_respuesta = nivel
                                return participante
                    else:
                            for key, value in valor.items():
                                if key == nivel:
                                    participante.bolsa = value + participante.bolsa
                                    participante.numero_respuesta = nivel
                                    return participante
                else:
                        participante.bolsa = 0
                        participante.numero_respuesta = nivel
                        time.sleep(1)
                        print('     Ah tu respuesta ha sido incorrecta, que mal acabas de perder la opotunidad de tu vida. \n')
                        print('     GAME OVER \n')
                        return participante
    elif nivel == 5: #Ciencia 
        categoria_uno = {
            1: '¿Cómo se llaman las células nerviosas?',
            2: '¿Qué fabricó Alessandro Volta, por primera vez, en 1800?',
            3: '¿Cuál es el pájaro símbolo de la paz?',
            4: '¿En qué mes el sol está más cerca de la Tierra?',
            5: '¿En qué parte del cuerpo se encuentra la piel más gruesa?'
        }
        respuestas_uno = [['Sinapticas','Neuronas','Axiomas','Espermatozoide'],
                        ['Pila','Bombilla','Bateria','Electricidad'],
                        ['Albatros','Paloma','Grulla','Monje'],
                        ['Julio','Diciembre','Agosto','Septiembre'],
                        ['Codos', 'Planta del pie', 'Espalda','Cara']]
        respuestas_uno_correcta = ['Neuronas','Pila','Paloma','Diciembre','Espalda']
        pregunta = None
        correcta = None
        i = random.randrange(1,5)

        for key, value in categoria_uno.items():
            if i == key:
                pregunta = value
                correcta = respuestas_uno_correcta[i-1]
        answer = respuestas_uno[i-1]
        answer = random.sample(answer, len(answer))

        print(f'     {pregunta} \n')
        print(f'     A. {answer[0]}     B. {answer[1]}')
        print(f'     C. {answer[2]}     D. {answer[3]} \n')
        answer_jugador = input('      Ingresa por favor la letra que corresponda a tu respuesta: ')
        print('     \n')

        x = True
        while x:
            if (answer_jugador == 'a' or answer_jugador == 'A'):
                answer_jugador = 0
                x = False
            elif (answer_jugador == 'b' or answer_jugador == 'B'):
                answer_jugador = 1
                x = False
            elif (answer_jugador == 'c' or answer_jugador == 'C'):
                answer_jugador = 2
                x = False
            elif (answer_jugador == 'd' or answer_jugador == 'D'):
                answer_jugador = 3
                x = False
            else:
                answer_jugador = input('      Hubo un error, ingresa nuevamente la letra que corresponda a tu respuesta: ')
                print('     \n')
        for ans in answer:
            if (ans == answer[answer_jugador]):
                if(answer[answer_jugador] == correcta):
                    print(f'     ¡Muy bien! Acabas de ganar {valor[nivel]} \n')
                    if participante.bolsa == 0:
                        for key, value in valor.items():
                            if key == nivel:
                                participante.bolsa = value
                                participante.numero_respuesta = nivel
                                return participante
                    else:
                            for key, value in valor.items():
                                if key == nivel:
                                    participante.bolsa = value + participante.bolsa
                                    participante.numero_respuesta = nivel
                                    return participante
                else:
                        participante.bolsa = 0
                        participante.numero_respuesta = nivel
                        time.sleep(1)
                        print('     Ah tu respuesta ha sido incorrecta, que mal acabas de perder la opotunidad de tu vida. \n')
                        print('     GAME OVER \n')
                        return participante
    else:
        print('Abandonaste')
        exit()