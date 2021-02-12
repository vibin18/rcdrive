import drive
import steering
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

while True:
  steering.left()
  time.sleep(2)
  steering.straight()
  time.sleep(2)
  steering.right()
  time.sleep(2)
  GPIO.cleanup()
  

