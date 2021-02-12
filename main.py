import drive
import steering
import time
import RPi.GPIO as GPIO

while True:
  steering.steer.left()
  time.sleep(2)
  steering.steer.straight()
  time.sleep(2)
  steering.steer.right()
  time.sleep(2)

