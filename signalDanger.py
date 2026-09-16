import serial
import time
from redconfig import read_port
connected=False
def send_signal(state):
    global connected
    arduino = serial.Serial(read_port(), 9600, timeout=1)
    time.sleep(3)

    if state:
        arduino.write(b'danger\n')
    else:
        arduino.write(b'safe\n')
    print(f"Сигнал отправлен: {'ВКЛ' if state else 'ВЫКЛ'}")
    # arduino.close()