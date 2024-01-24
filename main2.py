import os
import json
import pygame
from pygame.locals import QUIT
from moviepy.editor import VideoFileClip

def cargar_lista_reproduccion(json_path):
    with open(json_path, 'r') as file:
        playlist = json.load(file)
    return playlist

def reproducir_video(video_path, screen):
    clip = VideoFileClip(video_path)

    # Establecer el tamaÃ±o de la pantalla segÃºn las dimensiones del video
    screen = pygame.display.set_mode(clip.size)

    # Reproducir video
    clip.preview(fullscreen=True, audio=True)

def main():
    pygame.init()
    pygame.display.set_caption("Reproductor de Videos")

    script_directory = os.path.dirname(__file__)
    videos_directory = os.path.join(script_directory, "videos")
    json_playlist_path = os.path.join(script_directory, "playlist.json")

    playlist = cargar_lista_reproduccion(json_playlist_path)

    # Obtener las dimensiones de la pantalla
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    
    for video_info in playlist:
        video_name = video_info["nombre"]
        video_path = os.path.join(videos_directory, video_name)

        reproducir_video(video_path, screen)

    pygame.quit()

if __name__ == "__main__":
    main()
