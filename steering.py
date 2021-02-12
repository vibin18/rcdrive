import RPi.GPIO as GPIO

class steer():
  def __init__(self, name, age):
    self.m2in1 = 22
    self.m2in2 = 27
    self.m2en = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(self.m2in1,GPIO.OUT)
    GPIO.setup(self.m2in2,GPIO.OUT)
    GPIO.setup(self.m2en,GPIO.OUT)
    p1=GPIO.PWM(self.m2en,100)
    p1.start(100)


  def right(self):
    GPIO.output(self.m2in1,GPIO.LOW)
    GPIO.output(self.m2in2,GPIO.HIGH)


  def left(self):
    GPIO.output(self.m2in1,GPIO.HIGH)
    GPIO.output(self.m2in2,GPIO.LOW)


  def straight(self):
    GPIO.output(self.m2in1,GPIO.LOW)
    GPIO.output(self.m2in2,GPIO.LOW)