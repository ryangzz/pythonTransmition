import os
import requests
import time
from tqdm import tqdm

class Spot:

    def __init__(self, url, name, typee) -> None:
        self.url = url
        self.name = name
        self.type = typee
        print('Me instanciaron desde la clase spot')

        # Verificar y crear la carpeta "videos" si no existe
        self.check_and_create_folder()
        ruta_completa = os.path.join("videos", name)
        if not os.path.isfile(ruta_completa):
          self.downloadSpot()
        else:
            print('el archivo: '+ name +' ya lo tenemos guardado')

    def check_and_create_folder(self):
        folder_name = "videos"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f'Carpeta "{folder_name}" creada exitosamente.')

    def downloadSpot(self):
        try:
            # Construir la ruta completa del archivo local
            local_path = os.path.join("videos", self.name)

            # Hacer la solicitud GET a la URL del video
            init_time = time.time()
            respuesta = requests.get(self.url, stream=True)

            # Verificar si la solicitud fue exitosa (código de estado 200)
            if respuesta.status_code == 200:
                # Obtener tamaño total del archivo en bytes
                total_tamanio = int(respuesta.headers.get('content-length', 0))
                barra_progreso = tqdm(total=total_tamanio, unit='B', unit_scale=True)

                # Abrir un archivo local para escribir el contenido del video
                with open(local_path, 'wb') as archivo_local:
                    # Iterar sobre los fragmentos del video y escribirlos en el archivo
                    for fragmento in respuesta.iter_content(chunk_size=128):
                        archivo_local.write(fragmento)
                        barra_progreso.update(len(fragmento))
                barra_progreso.close()
                print(f'El video ha sido descargado exitosamente como "{local_path}"')
                end_time = time.time()
                total = end_time - init_time
                print(f'Tiempo de ejecución de descarga: {total:.2f} segundos')
            else:
                print(f'Error al descargar el video. Código de estado: {respuesta.status_code}')
        except Exception as e:
            print(f'Error: {e}')
