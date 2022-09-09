import machine
import time
led=machine.Pin(2,machine.Pin.OUT)

for m in range(3):
    
    led.value(0) #enciende led
    print("enciende led")
    time.sleep(2)
    led.value(1) #apagamos el led
    print("apagamos led")
    led.value(0) #enciende led
    print("enciende led")
    time.sleep(2)
    led.value(1) #apagamos el led
    print("apagamos led")

   