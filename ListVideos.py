import requests
import json
import os

class ListVideos:
    
    listaActual = None

    def __init__(self, url) -> None:
        # Obtener la ruta del script actual
        script_directory = os.path.dirname(os.path.abspath(__file__))

        # Cambiar al directorio del script
        os.chdir(script_directory)

        self.url = url
        print('Me instanciaron desde la clase ListVideos')
        self.getVideosActuales()
        self.__listVideos = self.obtener_diccionario_videos()
        try:
            self.eliminar_videos_obsoletos()
        except ValueError as ve:
            print(f"Error al eliminar videos: {ve}")


    def obtener_diccionario_videos(self):
        try:
            # Realizar la petición GET
            response = requests.get(self.url, verify=False)
            # Verificar si la petición fue exitosa (código de estado 200)
            response.raise_for_status()
            # Obtener la lista de videos en formato JSON
            lista_videos = response.json()
            self.guardar_en_archivo(lista_videos)
            return lista_videos['videos']
        except requests.exceptions.RequestException as e:
            print(f"Error al realizar la petición: {e}")
            raise Exception(f"Error al realizar la petición: {e}")
            return None
        except ValueError as ve:
            print(f"Error al decodificar JSON: {ve}")
            return None

    def get_listVideos(self):
        return self.__listVideos

    def guardar_en_archivo(self, data):
        try:
            with open('playlist.json', 'w', encoding='utf-8') as archivo:
                json.dump(data, archivo, ensure_ascii=False, indent=2)
            print("Datos guardados correctamente en playlist.json")
        except Exception as e:
            print(f"Error al guardar en el archivo: {e}")

    def getVideosActuales(self):
        archivo_json = "playlist.json"
        # Intentar abrir y cargar el archivo JSON
        try:
            with open(archivo_json, "r") as archivo:
                data_json = json.load(archivo)
                self.listaActual = data_json
                print("Data JSON cargada exitosamente:")
                # print(self.listaActual)
        except FileNotFoundError:
            print(f"Error: El archivo no fue encontrado.")
            self.listaActual  = None
        except json.JSONDecodeError:
            print(f"Error: No se pudo decodificar el contenido JSON en .")
            self.listaActual = None
        except Exception as e:
            print(f"Error desconocido: {e}")
            self.listaActual = None

    def eliminar_videos_obsoletos(self):
        if self.listaActual is None:
            print("No se puede comparar con la lista actual. La lista actual no está disponible.")
            return

        videos_actuales = set(video["solofile"] for video in self.listaActual["videos"])
        videos_nuevos = set(video["solofile"] for video in self.__listVideos)

        videos_obsoletos = videos_actuales - videos_nuevos

        if not videos_obsoletos:
            print("No hay videos obsoletos para eliminar.")
            return

        carpeta_videos = "videos"

        for video_obsoleto in videos_obsoletos:
            ruta_video_obsoleto = os.path.join(carpeta_videos, video_obsoleto)
            try:
                os.remove(ruta_video_obsoleto)
                # os.system("pkill -f main.py")
                print(f"Video obsoleto eliminado: {video_obsoleto}")
                
            except FileNotFoundError:
                print(f"Error: El video obsoleto {video_obsoleto} no fue encontrado.")
            except Exception as e:
                print(f"Error al eliminar el video obsoleto {video_obsoleto}: {e}")
