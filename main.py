import os
import json
import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, K_ESCAPE
from pygame import freetype
from moviepy.editor import VideoFileClip

def cargar_lista_reproduccion(json_path):
    with open(json_path, 'r') as file:
        playlist = json.load(file)
    return playlist

def reproducir_video(video_path, screen, font):
    clip = VideoFileClip(video_path)

    # Renderizar el reproductor de video (puedes personalizar esto según tus necesidades)
    font.render_to(screen, (10, 10), "", (255, 255, 255))
    pygame.display.flip()

    # Reproducir video
    clip.preview(fullscreen=True, audio=True)

def reproducir_lista(playlist, videos_directory, screen, font):
    script_directory    = os.path.dirname(__file__)
    json_playlist_path  = os.path.join(script_directory, "playlist.json")

    if not playlist["reproduccion"]:
        # No hay videos para reproducir, mostrar mensaje en pantalla completa
        font.render_to(screen, (10, 10), "No hay informacion para mostrar ...", (255, 255, 255))
        pygame.display.flip()
        pygame.time.delay(5000)  # Esperar 5 segundos antes de salir
    else:
      for video_info in playlist["reproduccion"]:
          video_name = video_info["nombre"]
          video_path = os.path.join(videos_directory, video_name)

          # Verifica si el archivo de video existe antes de intentar reproducirlo
          if os.path.exists(video_path):
              reproducir_video(video_path, screen, font)
          else:
              print(f"El video {video_path} no existe. Ignorándolo.")

          # Verificar eventos para detener la reproducción
          for event in pygame.event.get():
              if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                  os.system("pkill -f main.py")
                  pygame.quit()
                  sys.exit()

          # Verificar si hay cambios en el archivo playlist.json después de cada reproducción
          nueva_playlist = cargar_lista_reproduccion(json_playlist_path)
          if nueva_playlist != playlist:
              # Reiniciar la reproducción desde el principio
              print("Se detectaron cambios en playlist.json. Reiniciando la lista de reproducción.")
              pygame.quit()
              main()
              break

def main():
    pygame.init()
    pygame.display.set_caption("Reproductor de Videos")

    script_directory    = os.path.dirname(__file__)
    videos_directory    = os.path.join(script_directory, "videos")
    json_playlist_path  = os.path.join(script_directory, "playlist.json")

    # Obtener las dimensiones de la pantalla
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Configurar el tipo de letra para el reproductor de video
    font = freetype.SysFont(None, 24)

    running = True
    while running:
        # Cargar la lista de reproducción al inicio de cada iteración
        playlist = cargar_lista_reproduccion(json_playlist_path)

        # Llamar a la función reproducir_lista con la lista cargada
        reproducir_lista(playlist, videos_directory, screen, font)

    pygame.quit()

if __name__ == "__main__":
    main()