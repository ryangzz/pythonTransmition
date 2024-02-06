import socket
import threading
import time
import requests
from Programation import Programation
import subprocess

class ConnectionHandler:
    def __init__(self):
        print('Iniciando script principal de conexión a Internet')
        self.internet_event = threading.Event()
        self.main_event = threading.Event()
        self.programation = None

    def check_internet(self):
        while True:
            try:
                socket.create_connection(("www.google.com", 80))
                self.internet_event.set()
            except OSError:
                self.internet_event.clear()
            time.sleep(10)

    def get_valid_url(self):
        while True:
            user_url = input("Ingresa la URL: ")
            try:
                response = requests.head(user_url, timeout=5)
                if response.status_code == 200:
                    return user_url
                else:
                    print(f"La URL {user_url} no retornó un status 200. Inténtalo de nuevo.")
            except requests.RequestException as e:
                print(f"No se pudo conectar a la URL {user_url}: {e}. Inténtalo de nuevo.")

    def main(self):
        internet_thread = threading.Thread(target=self.check_internet, daemon=True)
        internet_thread.start()
        while True:
            self.internet_event.wait()

            print("¡Conexión a Internet detectada!")
            print("Iniciando comprobación y descarga de nuevas programaciones ....")
            try:
                # Intenta evaluar la URL proporcionada directamente
                url = 'http://192.168.1.102/listvideo2'
                try:
                    response = requests.head(url, timeout=5)
                    if response.status_code == 200:
                        print(f"La URL {url} es válida.")
                    else:
                        print(f"La URL {url} no retornó un status 200. Se solicitará una nueva URL.")
                        url = self.get_valid_url()
                except requests.RequestException as e:
                    print(f"No se pudo conectar a la URL {url}: {e}. Se solicitará una nueva URL.")
                    url = self.get_valid_url()

                self.programation = Programation(url)
                # Señaliza al main_event para que main.py sepa que hay una nueva programación
                self.main_event.set()
            except Exception as e:
                print(f"Error: {e}")

            time.sleep(10)

connection_handler = ConnectionHandler()
connection_handler.main()
