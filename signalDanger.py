import serial
import time
from redconfig import read_port
def send_signal(state):
    arduino = serial.Serial(read_port(), 9600, timeout=1)
    time.sleep(1)
    if state:
        arduino.write(b'danger\n')
    else:
        arduino.write(b'safe\n')
    print(f"Сигнал отправлен: {'ВКЛ' if state else 'ВЫКЛ'}")
    arduino.close()