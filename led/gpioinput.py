import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(15, GPIO.IN)
while True:
    input_value = GPIO.input(15)
    if input_value == False:
        print("The button has been pressed.")
        while input_value == False:
            input_value = GPIO.input(15)
