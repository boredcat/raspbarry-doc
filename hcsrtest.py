import RPi.GPIO as GPIO
import time
import random
GPIO.setmode(GPIO.BOARD)

sleepTime=0.00015
runTime=1

Left_Trig_Pin = 38
Left_Echo_Pin = 40

Right_Trig_Pin = 35
Right_Echo_Pin = 37

Front_Trig_Pin = 31
Front_Echo_Pin = 33

IN1 = 11
IN2 = 12
IN3 = 13
IN4 = 15

GPIO.setup(IN1,GPIO.OUT)
GPIO.setup(IN2,GPIO.OUT)
GPIO.setup(IN3,GPIO.OUT)
GPIO.setup(IN4,GPIO.OUT)

GPIO.setup(Left_Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Left_Echo_Pin, GPIO.IN)

GPIO.setup(Right_Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Right_Echo_Pin, GPIO.IN)

GPIO.setup(Front_Trig_Pin, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(Front_Echo_Pin, GPIO.IN)

time.sleep(5)

def checkdist(Trig_Pin,Echo_Pin):
    GPIO.output(Trig_Pin, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(Trig_Pin, GPIO.LOW)
    while not GPIO.input(Echo_Pin):
        pass
    t1 = time.time()
    while GPIO.input(Echo_Pin):
        pass
    t2 = time.time()
    return (t2-t1)*340*100/2

def init():
	GPIO.setup(IN1,GPIO.OUT)
	GPIO.setup(IN2,GPIO.OUT)
	GPIO.setup(IN3,GPIO.OUT)
	GPIO.setup(IN4,GPIO.OUT)

def leftDis():
	return checkdist(Left_Trig_Pin,Left_Echo_Pin)

def rightDis():
	return checkdist(Right_Trig_Pin,Right_Echo_Pin)

def frontDis():
	return checkdist(Front_Trig_Pin,Front_Echo_Pin)

def advance(sleep_time):
	init()
	GPIO.output(IN1,GPIO.HIGH)
	GPIO.output(IN2,GPIO.LOW)
	GPIO.output(IN3,GPIO.HIGH)
	GPIO.output(IN4,GPIO.LOW)
	time.sleep(sleep_time)
	GPIO.cleanup((IN1,IN2,IN3,IN4))

def back(sleep_time):
	init()
	GPIO.output(IN1,GPIO.LOW)
	GPIO.output(IN2,GPIO.HIGH)
	GPIO.output(IN3,GPIO.LOW)
	GPIO.output(IN4,GPIO.HIGH)
	time.sleep(sleep_time)
	GPIO.cleanup((IN1,IN2,IN3,IN4))

def left(sleep_time):
	init()
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,GPIO.HIGH)
	GPIO.output(IN4,GPIO.LOW)
	time.sleep(sleep_time)
	GPIO.cleanup((IN1,IN2,IN3,IN4))

def right(sleep_time):
	init()
	GPIO.output(IN1,GPIO.HIGH)
	GPIO.output(IN2,GPIO.LOW)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)
	time.sleep(sleep_time)
	GPIO.cleanup((IN1,IN2,IN3,IN4))

try:
    while True:
        if leftDis() <= 30 :
        	GPIO.cleanup((IN1,IN2,IN3,IN4))
        	print "right"
        	right(runTime)
        elif rightDis() <=30:
        	GPIO.cleanup((IN1,IN2,IN3,IN4))
        	print "left"
        	left(runTime)
        elif frontDis() <=50 and (leftDis()>=30 or rightDis()>=30):
        	GPIO.cleanup((IN1,IN2,IN3,IN4))
        	back(0.33)
        	if leftDis()>rightDis():
        		print "left"
        		left(runTime)
        	else:
        		print "right"
        		right(runTime)
        elif frontDis() <=50 and leftDis()<30 and rightDis()<30:
        	GPIO.cleanup((IN1,IN2,IN3,IN4))
        	back(0.33)
        	print "back"
        else :
        	
        	print "advance"
        	advance(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
