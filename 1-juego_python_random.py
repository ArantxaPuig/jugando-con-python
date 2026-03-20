#1. Importamos librería para números aleatorios
import random

#2. Mensaje de bienvenida
print("🎮 Bienvenido/a a: Adivina el número🎮")

#3. Variable para controlar si el jugador quiere repetir el juego
seguir_jugando = "s"

#4. Bucle principal: mientras el jugador quiera jugar
while seguir_jugando == "s":

    #5. Generar número secreto aleatorio entre 1 y 100
    numero_secreto = random.randint(1, 100)

    #6. Inicializar contador de intentos
    intentos = 0

    #7. Bucle hasta que el jugador adivine el número
    while True:

        #8. Intentar convertir input a número
        try:
            numero_usuario = int(input("Introduce un número entre 1 y 100: "))

            #9. Validar rango
            if numero_usuario < 1 or numero_usuario > 100:
                print("⚠️ El número debe estar entre 1 y 100")
                continue  # Volver al inicio del bucle

            #10. Contador de intentos
            intentos += 1

            #11. omparar número del jugador con el secreto
            if numero_usuario < numero_secreto:
                print("⬆ MÁS")
            elif numero_usuario > numero_secreto:
                print("⬇ MENOS")
            else:
                print(f"🎉 ¡Correcto! Lo lograste en {intentos} intentos")
                break  # Salir del bucle interno

        #12. Captura error si no es número
        except ValueError:
            print("❌ Debes introducir un número válido")

    #13. Preguntar si quiere jugar otra vez
    seguir_jugando = input("¿Quieres jugar otra vez? (s/n): ").lower()

#14. Mensaje final
print("Gracias por jugar. ¡Hasta la próxima!")