try:
	from gpiozero import LED
	from time import sleep
	import sys

	print('========================================')
	print('|              Blink LED               |')
	print('|    ------------------------------    |')
	print('|         LED connect to BOARD11       |')
	print('|                          PythonCoder8|')
	print('========================================')

	blinking_speed_str = input('How fast do you want your LED to blink on your breadboard (in milliseconds)? ')

	try:
		blinking_speed_int = int(blinking_speed_str)
	except:
		sys.exit('')

	del sys
	led = LED('BOARD11')

	while True:
		led.on()
		sleep(blinking_speed_int / 1000)
		led.off()
		sleep(blinking_speed_int / 1000)
except KeyboardInterrupt:
	print('')
	print('Exiting program...')
	print('')
