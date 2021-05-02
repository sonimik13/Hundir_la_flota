import numpy as np
import utils as ut
import constants as ct


print("-BATTLESHIP-\n")


print(r"""                                   )___(
                           _______/__/_
                  ___     /===========|   ___
 ____       __   [\\\]___/____________|__[///]   __
 \   \_____[\\]__/___________________________\__[//]___
  \     Sonia & Tito BattleShip Game Developers        /                                         
   \                                                  /
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                """)

print("""Hundir la flota
1. El juego se jugará contra la máquina (modalidad 1 jugador-máquina).
2. La flota estará formada por:
    a. Un destructor: 4 piezas
    b. 2 portaaviones: 3 piezas
    c. 3 fragatas: 2 piezas
    d. 4 submarinos: 1 pieza
3. Empieza a jugar el jugador. Se recogen las coordenadas y se comprueba
en el tablero de la máquina si hay barco. 
    a. Si hay barco, se muestra en el tablero con los impactos que has hecho 
    en la máquina como X, impacto. Sigues jugando hasta que falles.
    b. Si no hay barco, se muestra en el tablero con los impactos que has hecho  
    en la máquina como A, agua. Pasa a jugar la máquina, escoge una coordenada
    aleatoria y comprueba en el tablero del usuario si hay barco. Se repite el
    mismo proceso que con el jugador.
4.  Se continua el juego hasta que uno de los 2 jugadores se quede sin barcos.\n\n""")

tablero_usuario = ut.inicializar_tablero_usuario()

tablero_maquina = np.full(fill_value=' ', shape=(10, 10))

tablero_maquina = ut.colocar_barcos_maquina(4, 1, tablero_maquina)
tablero_maquina = ut.colocar_barcos_maquina(3, 2, tablero_maquina)
tablero_maquina = ut.colocar_barcos_maquina(2, 3, tablero_maquina)
tablero_maquina = ut.colocar_barcos_maquina(1, 4, tablero_maquina)

print(tablero_maquina)

ut.tablero_usuario_guard = np.full((10, 10), " ")

ut.tablero_maquina_guard = np.full((10, 10), " ")

ut.juego(tablero_maquina)

