# Mensaje de Bienvenida
print("Bienvenid@s a Par o Impar")
print("Introduce un número y te diré si es par o impar.")
# Juego
while True:
    try:
        numero_par = int(input("Escribe un número:"))
        if numero_par % 2 == 0:
            print(f"El número {numero_par} es par.")
        else:
            print(f"El número {numero_par} es impar.")
   
    except ValueError:
            print("Eso no es un número válido. Inténtalo de nuevo.")




