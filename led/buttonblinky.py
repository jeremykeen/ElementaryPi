import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(15, GPIO.IN)

pinNumLED = 11
btnOn = False
prev_input = 1

while True:
    try:
        input = GPIO.input(15)

        if ((not prev_input) and input):
            btnOn = not btnOn
        prev_input=input
        sleep(0.05)
        
        ## When the button is pressed, start toggling the LED between 
        ## HIGH and LOW with a 0.5s interval between
        if btnOn:
            GPIO.output(pinNumLED,GPIO.HIGH)
            sleep(0.5)
            GPIO.output(pinNumLED,GPIO.LOW)
            sleep(0.5)
        else:
            GPIO.output(pinNumLED,GPIO.HIGH)
