from gpiozero import LEDBoard
from time import sleep
from signal import pause
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('app.log', mode='w')
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

print('=================================================')
print('|                   LEDBoard                    |')
print('|  -------------------------------------------  |')
print('|            Use 220 ohm resistors              |')
print('|         Connect LED cathode to GND            |')
print('|         Uses pulse-width modulation           |')
print('|        Click Ctrl + C to exit program         |')
print('|------------------------------------------------')
print('|                                   PythonCoder8|')
print('=================================================')

try:
    leds = LEDBoard(5, 6, 13, pwm=True)
    while True:
        leds.value = (1, 1, 1)
        sleep(0.03)

        leds.value = (0.9, 0.9, 0.9)
        sleep(0.03)

        leds.value = (0.8, 0.8, 0.8)
        sleep(0.03)

        leds.value = (0.7, 0.7, 0.7)
        sleep(0.03)

        leds.value = (0.6, 0.6, 0.6)
        sleep(0.03)

        leds.value = (0.5, 0.5, 0.5)
        sleep(0.03)

        leds.value = (0.4, 0.4, 0.4)
        sleep(0.03)

        leds.value = (0.3, 0.3, 0.3)
        sleep(0.03)

        leds.value = (0.2, 0.2, 0.2)
        sleep(0.03)

        leds.value = (0.1, 0.1, 0.1)
        sleep(0.03)

        leds.value = (0, 0, 0)
        sleep(0.75)

except KeyboardInterrupt:
    print('\nExiting program...')

except Exception as exception:
    logger.exception('Encountered unhandled exception\n %s', exception)