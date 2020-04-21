import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

IN1=11
IN2=12
IN3=13
IN4=15

def init():
	GPIO.setup(IN1,GPIO.OUT)
	GPIO.setup(IN2,GPIO.OUT)
	GPIO.setup(IN3,GPIO.OUT)
	GPIO.setup(IN4,GPIO.OUT)

def advance(sleep_time):
	GPIO.output(IN1,GPIO.HIGH)
	GPIO.output(IN2,GPIO.LOW)
	GPIO.output(IN3,GPIO.HIGH)
	GPIO.output(IN4,GPIO.LOW)
	time.sleep(sleep_time)
	GPIO.cleanup()

def back(sleep_time):
	GPIO.output(IN1,GPIO.LOW)
	GPIO.output(IN2,GPIO.HIGH)
	GPIO.output(IN3,GPIO.LOW)
	GPIO.output(IN4,GPIO.HIGH)
	time.sleep(sleep_time)
	GPIO.cleanup()

def left(sleep_time):
	GPIO.output(IN1,False)
	GPIO.output(IN2,False)
	GPIO.output(IN3,GPIO.HIGH)
	GPIO.output(IN4,GPIO.LOW)
	time.sleep(sleep_time)
	GPIO.cleanup()

def right(sleep_time):
	GPIO.output(IN1,GPIO.HIGH)
	GPIO.output(IN2,GPIO.LOW)
	GPIO.output(IN3,False)
	GPIO.output(IN4,False)
	time.sleep(sleep_time)
	GPIO.cleanup()

init()
right(2)
