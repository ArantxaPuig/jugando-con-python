def pedir_numero():

#Pide un número al usuario que sea entero
   
    while True:
        try:
            numero = int(input("Introduce un número: "))
            return numero
        except ValueError:
            print("❌ Eso no es un número válido. Inténtalo de nuevo.")

def es_par(numero):
   
#Devuelve True si el número es par, False si es impar.

    return numero % 2 == 0

def mostrar_resultado(numero, es_par_num):
   
#Muestra si el número es par o impar.
   
    if es_par_num:
        print(f"✅ El número {numero} es Par")
    else:
        print(f"✅ El número {numero} es Impar")

# Lista de personas prohibidas
prohibidos = ["Juan", "Carlos"]

# Pedir nombre del jugador
nombre = input("Hola, ¿cómo te llamas?: ").strip()

if nombre in prohibidos:
    print(f"Lo siento {nombre}, no puedes jugar a Par o Impar.")
else:
    print(f"¡Bienvenido/a {nombre}! 🎲 Vamos a jugar a Par o Impar 🎲")
    seguir_jugando = "s"

    while seguir_jugando == "s":
        # Pedir número
        numero = pedir_numero()

        # Comprobar par o impar
        resultado = es_par(numero)

        # Mostrar resultado
        mostrar_resultado(numero, resultado)

        # Preguntar si quiere jugar otra vez
        seguir_jugando = input("¿Quieres jugar otra vez? (s/n): ").lower()

    print("Gracias por jugar. ¡Nos vemos!")