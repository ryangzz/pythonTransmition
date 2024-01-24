import os
import json
import pygame
from pygame.locals import QUIT
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
    clip.preview(fullscreen=True, audio=False)

def main():
    pygame.init()
    pygame.display.set_caption("Reproductor de Videos")

    script_directory = os.path.dirname(__file__)
    videos_directory = os.path.join(script_directory, "videos")
    json_playlist_path = os.path.join(script_directory, "playlist.json")

    playlist = cargar_lista_reproduccion(json_playlist_path)

    # Obtener las dimensiones de la pantalla
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Configurar el tipo de letra para el reproductor de video
    font = freetype.SysFont(None, 24)

    for video_info in playlist:
        video_name = video_info["nombre"]
        video_path = os.path.join(videos_directory, video_name)

        reproducir_video(video_path, screen, font)

    pygame.quit()

if __name__ == "__main__":
    main()
