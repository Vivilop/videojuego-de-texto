print('Bienvenido al video juego de texto')

import os

# Define el laberinto
laberinto = [
    "#####################################",
    "#P  #    #          #           #  #",
    "# # ###### ##### ## #### ##### # # #",
    "# #    #   #   # #    #       # # #",
    "# #### # ##### # ######### ##### # #",
    "#    #   #   #        #    #       #",
    "#####################################"
]

# Encuentra las coordenadas iniciales del jugador
def encontrar_posicion_jugador():
    for i in range(len(laberinto)):
        for j in range(len(laberinto[i])):
            if laberinto[i][j] == 'P':
                return i, j

# Muestra el laberinto en la consola
def mostrar_laberinto():
    os.system('cls' if os.name == 'nt' else 'clear')
    for fila in laberinto:
        print(fila)

# Mueve al jugador en el laberinto
def mover_jugador(dx, dy):
    x, y = encontrar_posicion_jugador()
    nuevo_x, nuevo_y = x + dx, y + dy

    # Comprueba si el movimiento es válido
    if 0 <= nuevo_x < len(laberinto) and 0 <= nuevo_y < len(laberinto[0]) and laberinto[nuevo_x][nuevo_y] != '#':
        laberinto[x] = laberinto[x][:y] + ' ' + laberinto[x][y+1:]
        laberinto[nuevo_x] = laberinto[nuevo_x][:nuevo_y] + 'P' + laberinto[nuevo_x][nuevo_y+1:]
        return True
    return False

# Bucle principal del juego
while True:
    mostrar_laberinto()

    # Comprobar si el jugador ha llegado a la salida
    if 'S' not in laberinto[-1]:
        print("¡Has llegado a la salida!")
        break

    movimiento = input("Utiliza las teclas ↑ ↓ ← → para mover al personaje (q para salir): ").lower()

    if movimiento == 'q':
        break
    elif movimiento == '↑':
        mover_jugador(-1, 0)
    elif movimiento == '↓':
        mover_jugador(1, 0)
    elif movimiento == '←':
        mover_jugador(0, -1)
    elif movimiento == '→':
        mover_jugador(0, 1)

print("¡Gracias por jugar!")
