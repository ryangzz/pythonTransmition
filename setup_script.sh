#!/bin/bash
sudo apt-get update
sudo apt-get install git 
# Contraseña con punto al final
PASSWORD="U%z6drNknTc6"

# Cambiarse al escritorio
cd ~/Desktop

# Clonar el repositorio
git clone https://tvrutaraspberry:${PASSWORD}@repo.eiimt.mx/digitalfactory/tvruta-python.git

# Entrar al proyecto
cd tvruta-python

# Cambiarse a la rama master-qa
git checkout master

# Instalar virtualenv
sudo pip install virtualenv

# Crear y activar el entorno virtual
virtualenv playSpots
source playSpots/bin/activate

# Instalar las bibliotecas requeridas
pip install pygame
pip install moviepy
pip install imageio[ffmpeg]
pip install numpy
pip install requests
pip install tqdm
# Instalar dependencias adicionales
sudo apt-get install libopenblas-dev
sudo apt-get install libsdl2-mixer-2.0-0
sudo apt-get install ffmpeg
sudo apt-get install libsdl2-ttf-2.0-0

# Crear el archivo .desktop
echo "[Desktop Entry]
Type=Application
Exec=lxterminal -e \"/home/pi/Desktop/tvruta-python/playSpots/bin/python /home/pi/Desktop/tvruta-python/conectionInternet.py\"
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=My-Cool-App3
Name=My-Cool-App3
Comment[en_US]=My Cool App 3 Description
Comment=My Cool App 3 Descripción" | sudo tee /etc/xdg/autostart/My-Cool-App3.desktop

# Crear el archivo .desktop
echo "[Desktop Entry]
Type=Application
Exec=lxterminal -e \"/home/pi/Desktop/tvruta-python/playSpots/bin/python /home/pi/Desktop/tvruta-python/main.py\"
Hidden=false
NoDisplay=false
X-GNOME-Autostart-enabled=true
Name[en_US]=My-Cool-App2
Name=My-Cool-App2
Comment[en_US]=My Cool App 2 Description
Comment=My Cool App 2 Descripción" | sudo tee /etc/xdg/autostart/My-Cool-App2.desktop
echo -e "[Desktop Entry]\nType=Application\nName=NAME OF APP\nComment=WHAT DOES IT DO?\nNoDisplay=false\n#Exec=chromium-browser --noerrdialogs --autoplay-policy=no-user-gesture-required --kiosk --disable-translate ~/Desktop/tvruta/index.html\nNotShowIn=GNOME;KDE;XFCE;" | sudo tee /etc/xdg/autostart/My-Cool-App.desktop"
#reiniciar
sudo reboot now
