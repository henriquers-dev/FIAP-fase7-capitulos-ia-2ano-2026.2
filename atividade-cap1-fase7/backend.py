from machine import Pin
import time
import random

led = Pin(2, Pin.OUT)

while True:
    bpm = random.randint(60, 120)
    temperatura = round(random.uniform(36, 38), 1)

    print("CardioIA - Monitoramento")
    print("BPM:", bpm)
    print("Temperatura:", temperatura)

    # Alerta demonstrativo, não clínico
    alerta = bpm > 100 or temperatura > 37.5

    led.value(1 if alerta else 0)

    print("Alerta simulado:", alerta)
    time.sleep(2)