import requests
import time
from tqdm import tqdm

def descargar_video(url, nombre_archivo):
    try:
        # Hacer la solicitud GET a la URL del video
        init_time = time.time()
        respuesta = requests.get(url, stream=True)

        # Verificar si la solicitud fue exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Obtener tamaño total del archivo en bytes
            total_tamanio = int(respuesta.headers.get('content-length', 0))
            barra_progreso = tqdm(total=total_tamanio, unit='B', unit_scale=True)

            # Abrir un archivo local para escribir el contenido del video
            with open(nombre_archivo, 'wb') as archivo_local:
                # Iterar sobre los fragmentos del video y escribirlos en el archivo
                for fragmento in respuesta.iter_content(chunk_size=128):
                    archivo_local.write(fragmento)
                    barra_progreso.update(len(fragmento))

            barra_progreso.close()
            print(f'El video ha sido descargado exitosamente como "{nombre_archivo}"')

            end_time = time.time()
            total = end_time - init_time
            print(f'Tiempo de ejecución de descarga: {total:.2f} segundos')
        else:
            print(f'Error al descargar el video. Código de estado: {respuesta.status_code}')
    except Exception as e:
        print(f'Error: {e}')

# URL del video
url_video = "https://itvu.tvruta.com/storage/videos/video_spot-video-spray-heridas-sa_1678292460.webm"

# Nombre del archivo local donde se guardará el video
nombre_archivo_local = "video_descargado.webm"

# Llamar a la función para descargar el video
descargar_video(url_video, nombre_archivo_local)
