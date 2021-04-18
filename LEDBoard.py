from gpiozero import LEDBoard
from time import sleep
from signal import pause

leds = LEDBoard(6, 5, 13, pwm=True)
while True:
    leds.value = (1, 1, 1)
    sleep(1)
    leds.value = (0.5, 0.5, 0.5)
    sleep(1)
    leds.value = (0, 0, 0)
    sleep(1)