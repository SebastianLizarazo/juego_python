# Juego de Disparos con Pygame

Este proyecto es un sencillo juego desarrollado en Python utilizando la librería **Pygame**. El objetivo del juego es destruir a todos los enemigos disparando láseres desde el avión del jugador.

## Funcionalidades

- **Jugador:**  
  - Representado por una imagen de un avión.
  - Se mueve horizontalmente siguiendo la posición del mouse.
  - Dispara láseres al hacer clic con el mouse.

- **Enemigos:**  
  - Se organizan en una formación de 3 filas y 10 columnas.
  - Se mueven de lado a lado; la dirección se invierte al llegar a los bordes de la pantalla.
  
- **Láseres:**  
  - Se disparan desde la posición del jugador.
  - Se mueven hacia arriba y al impactar con un enemigo se eliminan, aumentando el puntaje.
  
- **Fondo:**  
  - Muestra estrellas blancas y amarillas que se mueven verticalmente, simulando un efecto de desplazamiento.
  
- **Sonido:**  
  - Se reproduce un efecto de sonido cada vez que se dispara un láser.

- **Estado del juego:**  
  - Pantalla de inicio: Se muestra un mensaje invitando a iniciar el juego.
  - Pantalla de victoria: Al destruir todos los enemigos, se muestra el puntaje y se invita a reiniciar la partida.

## Requisitos

- Python 3.x
- [Pygame](https://www.pygame.org/)  
  (Los requisitos se pueden instalar utilizando el archivo `requirements.txt`)

## Instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/tu-usuario/tu-repositorio.git
