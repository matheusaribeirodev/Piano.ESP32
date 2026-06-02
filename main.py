import machine
import time

led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(12, machine.Pin.OUT)
led3 = machine.Pin(13, machine.Pin.OUT)

botao1 = machine.Pin(21, machine.Pin.IN, machine.Pin.PULL_UP)
botao2 = machine.Pin(26, machine.Pin.IN, machine.Pin.PULL_UP)
botao3 = machine.Pin(33, machine.Pin.IN, machine.Pin.PULL_UP)

def apagar_todos():
    led1.off()
    led2.off()
    led3.off()

while True:
    if botao1.value() == 0:
        while botao1.value() == 0:
         apagar_todos()
         led1.on()
         time.sleep(3)

         apagar_todos()
         led2.on()
         time.sleep(5)

         apagar_todos()
         led3.on()
         time.sleep(1)
         apagar_todos

    if botao2.value() == 0:
        while botao2.value() == 0:
         apagar_todos()
         led1.on()
         time.sleep(0.5)

         led2.on()
         time.sleep(0.5)

         led3.on()
         time.sleep(0.5)

         apagar_todos()
         time.sleep(0.5)

    if botao3.value() == 0:
        while botao3.value() == 0:
            led1.on()
            led2.on()
            led3.on()
            time.sleep(2)
            
            apagar_todos()
            time.sleep(1)
