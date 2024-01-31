import socket
import threading
import time
from Programation import Programation

def check_internet(event):
    while True:
        try:
            # Intenta hacer una conexión a un servidor externo (por ejemplo, Google)
            socket.create_connection(("www.google.com", 80))
            # Si la conexión tiene éxito, establece el evento
            event.set()
        except OSError:
            # Si hay un error (no hay conexión), limpia el evento
            event.clear()
        time.sleep(5)  # Espera 5 segundos antes de volver a verificar

def main():
    # Crea un evento
    internet_event = threading.Event()
  
    # Crea un hilo para la rutina de verificación de Internet
    internet_thread = threading.Thread(target=check_internet, args=(internet_event,), daemon=True)
    internet_thread.start()

    while True:
        # Espera hasta que el evento se active (indicando conexión a Internet)
        internet_event.wait()

        print("¡Conexión a Internet detectada!")
        print("iniciando comprobacion y descarga de nuevas programaciones ....")
        try:
          url = 'http://localhost/listvideo2'
          programacion = Programation(url)
        except Exception as e:
          print(f"Erroroooor: {e}")
        # Aquí puedes colocar cualquier acción que desees realizar cuando hay conexión a Internet
        # ...

        # Después de realizar las acciones, espera 5 segundos antes de volver a verificar
        time.sleep(10)

if __name__ == "__main__":
    main()
