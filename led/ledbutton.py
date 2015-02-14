import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

while True:
    input_value = GPIO.input(15)
    if input_value == False:
        print("The button has been pressed.")
        state == 1
	while (state == 1)
	    GPIO.output(11, True)
	    GPIO.output(16, False)
	    time.sleep(.1)
	    GPIO.output(11, False)
	    GPIO.output(16, True)
	    time.sleep(.1)
            while input_value == False
	        input_value = GPIO.input(15)
		if input_value == False:
			state == 0
			GPIO.output(11, False)
            		GPIO.output(16, False)
