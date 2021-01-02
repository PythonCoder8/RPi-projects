from gpiozero import LED, Button, PWMLED
from signal import pause

print('=================================================')
print('|            Button Controlled LED              |')
print('|  -------------------------------------------  |')
print('|            LED connect to BOARD11             |')
print('|         Button connect GND, BOARD12           |')
print('|                                   PythonCoder8|')
print('=================================================')


led = LED('BOARD11')
button = Button('BOARD12')
button.when_pressed = led.off
button.when_released = led.on

pause()