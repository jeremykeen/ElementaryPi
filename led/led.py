import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(11, False)
GPIO.output(16, True)
while True:
    GPIO.output(11, True)
    GPIO.output(16, False)
    time.sleep(.1)
    GPIO.output(11, False)
    GPIO.output(16, True)
    time.sleep(.1)


