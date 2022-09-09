import machine
from machine import Pin
import time
import bluetooth
from BLE import BLEUART
from time import sleep
from dht import DHT11


p23 = machine.Pin(5, machine.Pin.OUT)
sensorDHT= DHT11(Pin(16))
led1 = Pin(4, Pin.OUT)
led2 = Pin(15, Pin.OUT)
Buzzer = Pin(5, Pin.OUT)

name = 'Salguero'
ble = bluetooth.BLE()
uart = BLEUART(ble,name)


def on_rx():
    rx_buffer = uart.read().decode().strip()
    
#     uart.write('Menú'+ '\n')
#     uart.write('mario'+ '\n')
#     uart.write('navidad'+ '\n')
#     uart.write('dormir'+ '\n')
#     uart.write('temperatura'+ '\n')
#     uart.write('humedad'+ '\n')
    
    uart.write('Mensaje: '+ str(rx_buffer) + '\n')


#MARIO MELODY  
    
    if rx_buffer == 'mario':
        print("--REPRODUCIENDO LA MELODIA DE MARIO")
        uart.write('--REPRODUCIENDO LA MELODIA DE MARIO'+ '\n')
        play(p23, mario, 0.15, 512)
#         for m in range(4):
#             led1.value(1)
#             time.sleep(0.5)
#             led1.value(0)
#             time.sleep(0.5)
#             led2.value(1)
#             time.sleep(0.5)  
#             led2.value(0)

#NAVIDAD MELODY   
    
    if rx_buffer == 'navidad':
        print("--REPRODUCIENDO LA MELODIA DE NAVIDAD")
        uart.write('--REPRODUCIENDO LA MELODIA DE NAVIDAD '+ '\n')
        play(p23, navidad, 0.25, 512)

#DORMIR MELODY
    
    if rx_buffer == 'dormir':
        print("--REPRODUCIENDO LA MELODIA PARA DORMIR")
        uart.write('--REPRODUCIENDO LA MELODIA DE DORMIR'+ '\n')
        play(p23, dormir, 0.6, 512)

#TEMPERATURA

    if rx_buffer == 'temperatura':
        sensorDHT.measure()
        temp=sensorDHT.temperature()
        if temp>26:
            led2.value(1)
            print("T ={:02d} °C". format(temp))
            uart.write('T ={:02d} °C'. format(temp))
            uart.write('\n')
            print("CALUROSO")
            uart.write('CALUROSO')
            sleep(4)
            led2.off()
        if temp<25:
            led1.value(1)
            print("T ={:02d} °C". format(temp))
            uart.write('T ={:02d} °C'. format(temp))
            uart.write('\n')
            print("FRESCO")
            uart.write('FRESCO')
            sleep(4)
            led1.off()

#HUMEDAD

    if rx_buffer == 'humedad':
        sleep(1)
        sensorDHT.measure()
        hum=sensorDHT.humidity()
        print("h ={:02d}%". format(hum))
        uart.write('h ={:02d} %'. format(hum))
        led1.value(1)
        sleep(1)
        led1.off()

uart.irq(handler=on_rx)

B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
CS4 = 277
D4  = 294
DS4 = 311
E4  = 330
F4  = 349
FS4 = 370
G4  = 392
GS4 = 415
A4  = 440
AS4 = 466
B4  = 494
C5  = 523
CS5 = 554
D5  = 587
DS5 = 622
E5  = 659
F5  = 698
FS5 = 740
G5  = 784
GS5 = 831
A5  = 880
AS5 = 932
B5  = 988
C6  = 1047
CS6 = 1109
D6  = 1175
DS6 = 1245
E6  = 1319
F6  = 1397
FS6 = 1480
G6  = 1568
GS6 = 1661
A6  = 1760
AS6 = 1865
B6  = 1976
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951
C8  = 4186
CS8 = 4435
D8  = 4699
DS8 = 4978


def play(pin, melodies, delays, duty):
    pwm = machine.PWM(pin)
    for note in melodies:
        pwm.freq(note)
        pwm.duty(duty)
        time.sleep(delays)
    
    pwm.duty(0)
    
    pwm.deinit()


mario = [
     E7, E7,  0, E7,  0, C7, E7,  0,
     G7,  0,  0,  0, G6,  0,  0,  0,
     C7,  0,  0, G6,  0,  0, E6,  0,
      0, A6,  0, B6,  0,AS6, A6,  0,
     G6, E7,  0, G7, A7,  0, F7, G7,
      0, E7,  0, C7, D7, B6,  0,  0,
     C7,  0,  0, G6,  0,  0, E6,  0,
      0, A6,  0, B6,  0,AS6, A6,  0,
     G6, E7,  0, G7, A7,  0, F7, G7,
      0, E7,  0, C7, D7, B6,  0,  0,
]

navidad = [
    E7, E7, E7, 0,
    E7, E7, E7, 0,
    E7, G7, C7, D7, E7, 0,
    F7, F7, F7, F7, F7, E7, E7, E7, E7, D7, D7, E7, D7, 0, G7, 0,
    E7, E7, E7, 0,
    E7, E7, E7, 0,
    E7, G7, C7, D7, E7, 0,
    F7, F7, F7, F7, F7, E7, E7, E7, G7, G7, F7, D7, C7, 0 
]

dormir = [
    C6, C6, G6, G6, A6, A6, G6, 0,
    F6, F6, E6, E6, D6, D6, C6, 0,
    G6, G6, F6, F6, E6, E6, D6, 0,
    G6, G6, F6, F6, E6, E6, D6, 0,
    C6, C6, G6, G6, A6, A6, G6, 0,
    F6, F6, E6, E6, D6, D6, C6, 0,
]




while True:
    print("-----------------")
    print("Menú:")
    print("MARIO")
    print("NAVIDAD")
    print("DORMIR")
    print("TEMPERATURA")
    print("HUMEDAD")
    inicio=input('Ingrese palabra clave: ' )
    print("-----------------")
    
#MARIO MELODY
    
    if inicio=='MARIO':
        print("--REPRODUCIENDO LA MELODIA DE MARIO")
        uart.write('--REPRODUCIENDO LA MELODIA DE MARIO'+ '\n')
        play(p23, mario, 0.15, 512)
        
        
#NAVIDAD MELODY
  
    if inicio=='NAVIDAD':
        print("--REPRODUCIENDO LA MELODIA DE NAVIDAD")
        uart.write('--REPRODUCIENDO LA MELODIA DE NAVIDAD '+ '\n')
        play(p23, navidad, 0.25, 512)
  
#DORMIR MELODY 
  
    if inicio=='DORMIR':
        print("--REPRODUCIENDO LA MELODIA PARA DORMIR")
        uart.write('--REPRODUCIENDO LA MELODIA DE DORMIR'+ '\n')
        play(p23, dormir, 0.6, 512)

#TEMPERATURA

        
    if inicio=='TEMPERATURA':
        sensorDHT.measure()
        temp=sensorDHT.temperature()
        if temp>20:
            led2.value(1)
            print("T ={:02d} °C". format(temp))
            uart.write('T ={:02d} °C'. format(temp))
            uart.write('\n')
            print("CALUROSO")
            uart.write('CALUROSO')
            sleep(4)
            led2.off()
        if temp<19:
            led1.value(1)
            print("T ={:02d} °C". format(temp))
            uart.write('T ={:02d} °C'. format(temp))
            uart.write('\n')
            print("FRESCO")
            uart.write('FRESCO')
            sleep(4)
            led1.off()
#HUMEDAD 

    if inicio=='HUMEDAD':
        sleep(1)
        sensorDHT.measure()
        hum=sensorDHT.humidity()
        print("h ={:02d} %". format(hum))
        uart.write('h ={:02d} %'. format(hum))
        led1.value(1)
        sleep(1)
        led1.off()
        