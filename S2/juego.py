"""
adivinador de numeros

"""
import random

n_maximo = 0 #el numero maximo que se puede generar dependiendo de la dificultad seleccionada por el usuario
n_secreto = 0 #el numero secreto que el programa genera aleatoriamente dependiendo de la dificultad seleccionada por el usuario
n_intentos = 0  #cuantos intentos se han realizado en total
n_rondas = 0 #cuantas veces se ha iniciado una partida
dificultad = "" #dificultad seleccionada por el usuario
intento_nivel = 0 #cuantos intentos tiene en la dificultad seleccionada por el usuario
#estadisticas del juego
partidas_ganadas = 0 
partidas_perdidas = 0
mejor_puntaje = 0
n_intentos_facil = 0
n_intentos_medio = 0
n_intentos_dificil = 0
historial_intentos = "" #lista para guardar el historial de intentos del usuario en cada partida

# menu principal del juego
while True:
    print("""
1) selecciona una dificultad 
2) Ver estadísticas (partidas jugadas, ganadas, perdidas)
3) Ver instrucciones del juego
4) Salir del programa
          
""")
    opcion = input("ingrese una opcion: ")
    if opcion >= "1" and opcion <= "4":
        print(f"\nseleccionaste {opcion}\n")  
    else:
        print("opcion no valida, ingrese un numero entre 1 y 4")
# menu de seleccion de dificultad       
    match opcion:
        case "1":
            print("\ndificultad del juego:")
            print("1) facil")
            print("2) medio")
            print("3) dificil")

            while True: #validacion de la dificultad ingresada por el usuario
                dificultad = input("ingrese la dificultad: ")
                """

               if dificultad.isdigit():  # asi lo pense yo
                    dificultad = int(dificultad)
                    if dificultad >= 1 and dificultad <= 3:
                        print(f"seleccionaste {dificultad}")
                        break

                    else:
                        print(f"opcion no valida, ingrese un numero entre 1 y 3")
                        
                        """

# cual es la diferencia entre dejar en math dentro del ciclo while o fuera del ciclo while?

                match dificultad: #configuracion del juego dependiendo de la dificultad seleccionada por el usuario
                    case 1:
                        print("\ndificultad facil seleccionada")
                        print("el numero secreto esta entre 1 y 100")
                        print("tienes 10 intentos para adivinar el numero secreto")
                        n_intentos_facil += 1
                        n_rondas += 1
                        n_maximo = 100
                        n_secreto = random.randint(1, n_maximo)
                        dificultad = "facil"
                        intento_nivel = 10
                        print("nivel de detalle de pistas: hirviendo > caliente > tibio > frio > congelado ")
                        break
                    case 2:
                        print("\ndificultad media seleccionada")
                        print("el numero secreto esta entre 1 y 150")
                        print("tienes 7 intentos para adivinar el numero secreto")
                        n_intentos_medio += 1
                        n_rondas += 1
                        n_maximo = 150
                        n_secreto = random.randint(1, n_maximo)
                        dificultad = "medio"
                        intento_nivel = 7
                        print("nivel de detalle de pistas: > cerca > lejos > muy lejos > muy cerca ")
                        break
                    case 3:
                        print("\ndificultad dificil seleccionada")
                        print("el numero secreto esta entre 1 y 200")
                        print("tienes 5 intentos para adivinar el numero secreto")
                        n_intentos_dificil += 1
                        n_rondas += 1
                        n_maximo = 200
                        n_secreto = random.randint(1, n_maximo)
                        dificultad = "dificil"
                        intento_nivel = 5
                        print("nivel de detalle de pistas: > muy alto > muy bajo ")
                        break
                    case _:
                        print("opcion no valida, ingrese un numero entre 1 y 3")

#ciclo principal del juego
            for i in range(intento_nivel):
                print(f"intentos restantes: {intento_nivel - n_intentos}")
                print(f"historial de intentos: {historial_intentos=}")

                n_ingresado = input("ingresa el numero secreto: ")
                while True:#validacion del numero ingresado por el usuario
                    if n_ingresado.isdigit():
                        n_ingresado = int(n_ingresado)
                        if n_ingresado >= 1 and n_ingresado <= n_maximo:
                           
                            break

                        else:
                            print(f"opcion no valida, ingrese un numero entre 1 y {n_maximo}")

                

                n_intentos -= 1 #contador de intentos totales
                diferencia = abs(n_secreto - n_ingresado) #calculo de la diferencia entre el numero secreto y el numero ingresado por el 
                                                          #usuario para dar pistas mas detalladas dependiendo de la dificultad seleccionada
                historial_intentos += f"{n_ingresado}, " #lista para guardar el historial de intentos del usuario en cada partida
            else:
                    print("lo siento, has perdido")
                    print(f"el numero secreto era: {n_secreto}")
                    partidas_perdidas += 1

# cuando se pierde la partida

                    print(f"""
--- resumen de la partida ---
dificultad seleccionada: {dificultad}
numero secreto: {n_secreto}
tus intentos: {historial_intentos}
intentos realizados: {n_intentos} de {intento_nivel}    
resultado: perdiste
                          
                          

                          """)
# cuando se gana la partida 
            if n_ingresado == n_secreto:

                if n_intentos < mejor_puntaje or mejor_puntaje == 0:
                    mejor_puntaje = n_intentos

                    print(f"felicidades, has adivinado el numero secreto {n_secreto} en {n_intentos} intentos")
                    partidas_ganadas += 1
                    print(f"""
--- resumen de la partida ---
dificultad seleccionada: {dificultad}
numero secreto: {n_secreto}
tus intentos: {historial_intentos}
intentos realizados: {n_intentos} de {intento_nivel}    
resultado: ganaste




                    """)
                    break

                if dificultad == "facil": #pistas para la dificultad facil
                    if diferencia <= 5:
                        print(" 'hirviendo', estas cerca del numero secreto")
                    elif 6 <= diferencia <= 10:
                        print(" 'tibio', estas cerca del numero secreto")
                    elif 11 <= diferencia <= 20:
                        print(" 'frio', estas lejos del numero secreto")
                    elif diferencia >= 21: 
                        print(" 'congelado', estas muy lejos del numero secreto")

                if dificultad == "facil" or dificultad == "medio": #pistas para la dificultad facil y media
                    if diferencia <= 10:
                        print("estas cerca del numero secreto")
                    else:
                        print("estas lejos del numero secreto")

                if n_ingresado > n_secreto:#pistas para todos los niveles
                      print("el numero ingresado es mayor que el numero secreto")

                else:
                      print("el numero ingresado es menor que el numero secreto")
            historial_intentos = "" #reinicio del historial de intentos para la siguiente partida              

                    

            """    #revisar **** # 
aqui no sabia lo de abs para calcular la diferencia entre el numero secreto y el numero ingresado
por el usuario, asi que lo hice con if y elif, pero no se si esta bien o si hay una forma mas sencilla de hacerlo

                print(f"numero de intentos: {intento_nivel}")

                if n_ingresado < n_secreto:
                        print("el numero ingresado es menor que el numero secreto")
                        n_intentos += 1
                        intento_nivel -= 1
                                    
                elif n_ingresado > n_secreto:
                        print("el numero ingresado es mayor que el numero secreto")
                        n_intentos += 1
                        intento_nivel -= 1
                                    
                elif n_secreto == n_secreto:
                        print("felicidades, has adivinado el numero secreto")
                        partidas_ganadas += 1
                                    
                        break
                if n_intentos > n_intentos:
                        mejor_puntaje = n_intentos

                if n_intentos_facil > n_intentos_medio and n_intentos_facil > n_intentos_dificil:
                            dificultad_mas_jugada = "facil"
                elif n_intentos_medio > n_intentos_dificil:
                                    dificultad_mas_jugada = "medio"
                else:
                            dificultad_mas_jugada = "dificil"

            else:
                print("lo siento, has perdido")
                print(f"el numero secreto era: {n_secreto}")
                partidas_perdidas += 1
#revisar ****
"""


        case "2": #estadisticas del juego
            print(f"partidas jugadas: {n_rondas}")
            print(f"partidas ganadas: {partidas_ganadas} {partidas_ganadas/n_rondas*100:.2f}%")
            print(f"partidas perdidas: {partidas_perdidas} {partidas_perdidas/n_rondas*100:.2f}%")
            print(f"mejor puntaje: {mejor_puntaje}")
#         print(f"dificultad mas jugada: {}")
            print(f"partidas jugadas en dificultad facil: {n_intentos_facil} {n_intentos_facil/n_rondas*100:.2f}%")
            print(f"partidas jugadas en dificultad media: {n_intentos_medio} {n_intentos_medio/n_rondas*100:.2f}%")
            print(f"partidas jugadas en dificultad dificil: {n_intentos_dificil} {n_intentos_dificil/n_rondas*100:.2f}%")
        case "3": #instrucciones del juego
            print("instrucciones del juego:")
            print("1) el programa genera un numero secreto entre 1 y 100")
            print("2) el jugador tiene que adivinar el numero secreto")
            print("3) el jugador tiene 10 intentos para adivinar el numero secreto")
            print("4) el programa le dira al jugador si el numero ingresado es mayor o menor que el numero secreto")
        case "4": #salir del programa
                print("gracias por jugar")
                break                                      