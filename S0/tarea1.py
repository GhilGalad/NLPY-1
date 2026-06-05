"""
Mi Primer Programa en Python 
 
Funciones, Variables y Tipos de Datos

Calculadora de Propinas Personalizada

"""

#1 saludo personalizado

print("----bienvenidos a la calculadora de propinas----")
nombre = input("cual es tu nombre? ")

def saludar():

    nombre_formateado = nombre.capitalize()
    print(f"hola bienvenido {nombre_formateado}")


saludar() # ¿porque si le pongo aqui un nombre no me funciona?

def lineas_divisoras():
    print("-----------------------------")

lineas_divisoras() 
#validacion de datos 
moneda = 0

while True:
    if moneda <= 0 or moneda > 3:
        moneda = int(input("¿con cual monedas vas a pagar? -1 si es ₡ , -2 si es $, -3 si es €"))
    if moneda <= 0 or moneda > 3:
        print("los datos son incorrectos, intentalo de nuevo")
    if moneda > 0 and moneda <= 3:
        break


match moneda:
    case 1:
        moneda = "₡"
    case 2:
        moneda = "$"
    case 3:
        moneda = "€"

lineas_divisoras()

#2 recopilacion de datos
contador = 1
verificacion = 0
total_cuenta = float(input("¿cual es el monto total de la cuenta? "))

def validacion(contador): # validamos los datos dados por el usuario
    while True:
        match contador:
            case 1:
                if contador == 1:
                    verificacion = total_cuenta
            case 2: 
                if contador == 2:
                    verificacion = propina
            case 3: 
                if contador == 3:
                    verificacion = personas

        if verificacion <= 0:
            print("el monto ingresado no puede ser de 0, intentalo de nuevo")
            break
        else:
            contador += 1
            break

validacion(contador) #¿porque aqui me pide poner contador?

# mostrar el porcentaje de propinas
print(f"""
un 5% de propina seria:{total_cuenta * (5 / 100)}
un 10% de propina seria:{total_cuenta * (10 / 100)}
un 15% de propina seria:{total_cuenta * (15 / 100)}
un 20% de propina seria:{total_cuenta * (20 / 100)}
                                                             """)

propina = float(input("¿cual es el porcentaje de propina que quieres dejar? "))
validacion(contador)

personas = int(input("¿entre cuantas personas dividiran la cuenta? "))
validacion(contador)


#print(total_cuenta, propina, personas)
lineas_divisoras()

#3 calculos

total_propina = total_cuenta * (propina / 100)
propina_cuenta = total_cuenta + total_propina
pago_x_persona = propina_cuenta / personas

#propinas del 5,10,15 y 20%



# print(total_propina , propina_cuenta, pago_x_persona )

#4 presentacion de resultados

print(f"{nombre.capitalize()} aqui estan los datos")
lineas_divisoras()
print(f"el monto tatal de la cuenta es {moneda}{round(total_cuenta)}")
lineas_divisoras()
print(f"la propina es de {moneda}{round(total_propina)} {moneda}({round(propina)})")
lineas_divisoras()
print(f"la cuenta se divide entre {personas} personas ")
lineas_divisoras()
print(f"que seria un total a pagar de {moneda}{round(pago_x_persona)} por persona")
lineas_divisoras()




























