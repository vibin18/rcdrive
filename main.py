import * from drive
import * from steering
import time


while True:
  steering.left()
  time.sleep(2)
  steering.stop()
  time.sleep(2)
  steering.right()
  time.sleep(2)
  
