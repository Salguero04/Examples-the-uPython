from machine import Pin
import bluetooth
from BLE import BLEUART

led1 = Pin(4, Pin.OUT)
led2 = Pin(15, Pin.OUT)

name = 'ESP32'
ble = bluetooth.BLE()
uart = BLEUART(ble,name)

def on_rx():
    rx_buffer = uart.read().decode().strip()
    
    uart.write('Mensaje: '+ str(rx_buffer) + '\n')
    
    if rx_buffer == 'A':
        led1.on()
    if rx_buffer == 'B':
        led2.on()   
    if rx_buffer == 'C':
        led1.off()
    if rx_buffer == 'D':
        led2.off()


uart.irq(handler=on_rx)