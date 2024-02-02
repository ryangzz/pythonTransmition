import socket
import threading
import time
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

    def main(self):
        internet_thread = threading.Thread(target=self.check_internet, daemon=True)
        internet_thread.start()
        while True:
            self.internet_event.wait()

            print("¡Conexión a Internet detectada!")
            print("Iniciando comprobación y descarga de nuevas programaciones ....")
            try:
                url = 'http://localhost/listvideo2'
                self.programation = Programation(url)
                # Señaliza al main_event para que main.py sepa que hay una nueva programación
                self.main_event.set()
            except Exception as e:
                print(f"Error: {e}")

            time.sleep(10)

connection_handler = ConnectionHandler()
connection_handler.main()