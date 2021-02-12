import RPi.GPIO as GPIO

m2in1 = 22
m2in2 = 27
m2en = 17


class steer():
    def __init__(self, name, age):
      GPIO.setmode(GPIO.BCM)
      GPIO.setwarnings(False)
      GPIO.setup(m2in1,GPIO.OUT)
      GPIO.setup(m2in2,GPIO.OUT)
      GPIO.setup(m2en,GPIO.OUT)
      p1=GPIO.PWM(m2en,100)
      p1.start(100)


    def right():
      GPIO.output(m2in1,GPIO.LOW)
      GPIO.output(m2in2,GPIO.HIGH)


    def left():
      GPIO.output(m2in1,GPIO.HIGH)
      GPIO.output(m2in2,GPIO.LOW)


    def straight():
      GPIO.output(m2in1,GPIO.LOW)
      GPIO.output(m2in2,GPIO.LOW)