import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

GPIO.output(11, False)
GPIO.output(16, False)
