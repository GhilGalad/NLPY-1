"""
adivinador de numeros

"""
import random

n_maximo = 0
n_secreto = 0
n_intentos = 0
n_rondas = 0
dificultad = ""
partidas_ganadas = 0
partidas_perdidas = 0
mejor_puntaje = 0
n_intentos_facil = 0
n_intentos_medio = 0
n_intentos_dificil = 0

# menu Jugar una nueva partida
while True:
    print("""
1) selecciona una dificultad y juega una nueva partida
2) Ver estadísticas (partidas jugadas, ganadas, perdidas)
3) Ver instrucciones del juego
4) Salir del programa
          
""")
    opcion = input("ingrese una opcion: ")
    if opcion >= "1" and opcion <= "4":
        pass   
    else:
        print("opcion no valida, ingrese un numero entre 1 y 4")
        
    match opcion:
        case "1":
            n_intentos_facil = +1

            while True:
                n_rondas += 1

                print("dificultad del juego:")
                print("1) facil")
                print("2) medio")
                print("3) dificil")

                dificultad = input("ingrese la dificultad: ")


                if dificultad == "1":
                    n_maximo = 100
                    n_secreto = random.randint(1, n_maximo)

                    print("dificultad facil seleccionada")
                    print("el numero secreto esta entre 1 y 100")
                    print("tienes 10 intentos para adivinar el numero secreto")
                    print("buena suerte")

                    n_secreto = random.randint(1, n_maximo)
                    n_intentos = 9

                    for i in range(10):
                        n_ingresado = (input("ingresa el numero secreto: "))
                        while True:
                            if n_ingresado.isdigit():
                                n_ingresado = int(n_ingresado)
                                if n_ingresado >= 1 and n_ingresado <= n_maximo:
                                    print("opcion valida")
                                    break

                                else:
                                    print(f"opcion no valida, ingrese un numero entre 1 y {n_maximo}")

                        if n_ingresado < 1 or n_ingresado > n_maximo:
                            print(f"numero ingresado no valido, ingresa un numero entre 1 y {n_maximo}")
                            continue

                        print(f"numero de intentos: {n_intentos - i}")

                        if n_ingresado < n_secreto:
                            print("el numero ingresado es menor que el numero secreto")
                            n_rondas += 1
                            
                        elif n_ingresado > n_secreto:
                            print("el numero ingresado es mayor que el numero secreto")
                            n_rondas += 1
                            
                        elif n_secreto == n_secreto:
                            print("felicidades, has adivinado el numero secreto")
                            partidas_ganadas += 1
                            
                            break
                        if n_rondas > n_rondas:
                            mejor_puntaje = n_rondas

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


                    

                elif dificultad == "2":
                    n_intentos_medio = +1
                    n_maximo = 150
                    n_secreto = random.randint(1, n_maximo)
                    print("dificultad media seleccionada")
                    print("el numero secreto esta entre 1 y 150")
                    print("tienes 10 intentos para adivinar el numero secreto")
                    print("buena suerte")
                elif dificultad == "3":
                    n_intentos_dificil = +1
                    n_maximo = 200
                    n_secreto = random.randint(1, n_maximo)
                    print("dificultad dificil seleccionada")
                    print("el numero secreto esta entre 1 y 200")
                    print("tienes 10 intentos para adivinar el numero secreto")
                    print("buena suerte")

                if dificultad not in ["1", "2", "3"]:
                    print("dificultad no valida")
                    continue

                break
            

        
        case "2":
            print(f"partidas jugadas: {n_rondas}")
            print(f"partidas ganadas: {partidas_ganadas} {partidas_ganadas/n_rondas*100:.2f}%")
            print(f"partidas perdidas: {partidas_perdidas} {partidas_perdidas/n_rondas*100:.2f}%")
            print(f"mejor puntaje: {mejor_puntaje}")
            print(f"dificultad mas jugada: {dificultad_mas_jugada}")
            print(f"partidas jugadas en dificultad facil: {n_intentos_facil} {n_intentos_facil/n_rondas*100:.2f}%")
            print(f"partidas jugadas en dificultad media: {n_intentos_medio} {n_intentos_medio/n_rondas*100:.2f}%")
            print(f"partidas jugadas en dificultad dificil: {n_intentos_dificil} {n_intentos_dificil/n_rondas*100:.2f}%")
        case "3":
            print("instrucciones del juego:")
            print("1) el programa genera un numero secreto entre 1 y 100")
            print("2) el jugador tiene que adivinar el numero secreto")
            print("3) el jugador tiene 10 intentos para adivinar el numero secreto")
            print("4) el programa le dira al jugador si el numero ingresado es mayor o menor que el numero secreto")
        case "4":
            print("gracias por jugar")


        
            
            break                                           