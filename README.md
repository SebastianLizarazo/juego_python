# Juego de Disparos con Pygame
Proyecto hecho por Sebastian Lizarazo

# Descripción y funcionalidad
A través del archivo **game.py** se encuentra el código que ejecuta el videojuego, se establecieron tres clases:
**Player()**, **Enemy()**, **Laser()** y **Game()** estableciendo sus respectivos atributos y métodos. Se implementó la librería **PyGame** junto con **Random** para crear la funcionalidad del juego.

El fondo fue creado a partir de círculos de pequeño tamaño en posiciones aleatorias (representando estrellas) con su respectiva animación de caída, los enemigos se mueven a los lados a través del eje X, donde el jugador en la parte inferior de la ventana tendrá movimiento completo en el eje X a través del mouse.

La dimensión de la ventana está establecida para un monitor de resolución 720p.

Para iniciar una partida se debe dar clic a cualquier tecla, esto hará que se dé inicio y se cargue en la misma ventana a los enemigos y el fondo, aparte del jugador mismo, cada que se realice un clic con el mouse se disparará un láser que al entrar en contacto con un enemigo hará que tanto el láser como el enemigo desaparezcan y sume un punto al puntaje total que se mostrará al acabar la partida y para iniciar nuevamente tan solo se tendrá que presionar cualquier tecla.

Los métodos funcionales creados fueron: **process_events()**, **run_controller()** y **display_frame()**, todos parte de la clase Game que se ocupan de manejar los eventos durante la ejecución del programa, la lógica manejada por el programa y, el dibujo y actualización de la ventana, cada uno respectivamente.

## Requisitos
- Python 3.x
- [Pygame](https://www.pygame.org/)  
  

