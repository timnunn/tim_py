import RPi.GPIO as GPIO   # Import Rasberry Pi GPIO Library
from time import sleep    # Import the sleep function from the time module

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT, initial=GPIO.LOW)  #  set pin 24 to be an output pin.
#and set the initial value to low(off)

while True: #Run forever
    GPIO.output(24, GPIO.HIGH) #Turn on
    sleep(1)                    #Sleep for 1 second
    GPIO.output(24, GPIO.LOW)   #Turn Off
    sleep(1)                    #Sleep for 1 second