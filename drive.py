import RPi.GPIO as GPIO

in1 = 24
in2 = 23
en = 25

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p=GPIO.PWM(en,40)


p.start(100)

def forward():
  GPIO.output(in1,GPIO.HIGH)
  GPIO.output(in2,GPIO.LOW)
  

def backward():
  GPIO.output(in1,GPIO.LOW)
  GPIO.output(in2,GPIO.HIGH)
  

def stop():
  GPIO.output(in1,GPIO.LOW)
  GPIO.output(in2,GPIO.LOW)
  
