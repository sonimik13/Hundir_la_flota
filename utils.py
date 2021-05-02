import numpy as np
import random

def inicializar_tablero_usuario():
    """
    Función que posiciona los barcos del jugador en el tablero
    Inputs:
        ninguno
    Output:
        tablero_usuario: array
    """

    tablero_usuario = np.full((10, 10), " ")
    tablero_usuario[2, 2] = "O"
    tablero_usuario[6:9, 4] = "O"
    tablero_usuario[3:6, 8] = "O"
    tablero_usuario[4, 1:5] = "O"
    tablero_usuario[9, 6:8] = "O"
    tablero_usuario[:2, 7] = "O"
    tablero_usuario[8, 1:3] = "O"
    tablero_usuario[7, 8] = "O"
    tablero_usuario[0, 4] = "O"
    tablero_usuario[3, 6] = "O"

    return tablero_usuario

tablero_usuario = inicializar_tablero_usuario()
tablero_maquina = np.full(fill_value=' ', shape=(10, 10))

def colocar_barcos_maquina(eslora, num_barcos, tablero_maquina):
    """
    Función que posiciona los barcos de la máquina aleatoriamente en el tablero
    Inputs:
        eslora: longitud del barco (int)
        num_barcos: número de barcos (int)
        tablero_máquina: array
    Output:
        tablero_máquina: array
    """

    while num_barcos > 0:

        orient = random.choice(['N', 'S', 'E', 'O'])
        current_pos = np.random.randint(10, size=2)
        fila = current_pos[0]
        col = current_pos[1]

        coors_posiN = tablero_maquina[fila:fila - eslora:-1, col]
        coors_posiE = tablero_maquina[fila, col: col + eslora]
        coors_posiS = tablero_maquina[fila:fila + eslora, col]
        coors_posiO = tablero_maquina[fila, col: col - eslora:-1]

        if (orient == 'N') and (len(coors_posiN) == eslora) and ('O' not in coors_posiN):
            tablero_maquina[fila:fila - eslora:-1, col] = 'O'
            num_barcos = num_barcos - 1

        elif (orient == 'E') and (len(coors_posiE) == eslora) and ('O' not in coors_posiE):
            tablero_maquina[fila, col: col + eslora] = 'O'
            num_barcos = num_barcos - 1

        elif (orient == 'S') and (len(coors_posiS) == eslora) and ('O' not in coors_posiS):
            tablero_maquina[fila:fila + eslora, col] = 'O'
            num_barcos = num_barcos - 1

        elif (orient == 'O') and (len(coors_posiO) == eslora) and ('O' not in coors_posiO):
            tablero_maquina[fila, col: col - eslora:-1] = 'O'
            num_barcos = num_barcos - 1

    return tablero_maquina



def juego(tablero_maquina):
    """
    Función que realiza los disparos en los tableros jugador y máquina
    Inputs:
        tablero_máquina: array
    Output:
        ninguno
    """

    vidas_usu = 20

    vidas_maq = 20

    while True:

        try:

            fila_usu = int(input("Introduzca la fila de 0 a 9: \n"))

            col_usu = int(input("Introduzca la columna de 0 a 9: \n"))

            print("\n")

            while tablero_usuario_guard[fila_usu, col_usu] == ' ':

                if tablero_maquina[fila_usu, col_usu] == 'O':

                    tablero_usuario_guard[fila_usu, col_usu] = 'X'

                    print("\nTABLERO ENEMIGO: \n", tablero_usuario_guard)

                    print("\n")

                    print("\n¡Diste en el blanco!\n")

                    vidas_usu = vidas_usu - 1

                    if vidas_usu == 0:
                        print('\n¡¡ENHORABUENA!! Has ganado la partida!\n')

                        break

                else:

                    if tablero_maquina[fila_usu, col_usu] == ' ':
                        tablero_usuario_guard[fila_usu, col_usu] = 'A'

                        print("\nTABLERO ENEMIGO: \n ", tablero_usuario_guard)

                        print("\n")

                        print("\n!Has fallado¡ Tu disparo se fue al agua ...\n")

                    while True:

                        fila_maq = np.random.randint(10)

                        col_maq = np.random.randint(10)

                        if tablero_usuario[fila_maq, col_maq] == 'O':

                            tablero_maquina_guard[fila_maq, col_maq] = 'X'

                            print("\nTU TABLERO: \n", tablero_maquina_guard)

                            print("\n")

                            print("\nEl enemigo ha acertado.\n")

                            vidas_maq = vidas_maq - 1

                            if vidas_maq == 0:
                                print('\nEl enemigo te ha ganado ...\n')

                                break



                        else:

                            if tablero_usuario[fila_maq, col_maq] == ' ':
                                tablero_maquina_guard[fila_maq, col_maq] = 'A'

                                print("\nTU TABLERO: \n", tablero_maquina_guard)

                                print("\n")

                                print("\nEl enemigo ha fallado. Es tu turno.\n")

                                break
                break

        except (ValueError, IndexError):

            print("Caracter no valido\n")



        if vidas_usu == 0:

            break

        if vidas_maq == 0:

            break


