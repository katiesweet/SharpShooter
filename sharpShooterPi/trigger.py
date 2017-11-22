import RPi.GPIO as GPIO
import socket
from time import sleep


class motorControl:

	def __init__(self):
		GPIO.setmode(GPIO.BOARD)

		self.Motor1A = 16
		self.Motor1B = 18
		self.Motor1E = 22

		GPIO.setup(self.Motor1A,GPIO.OUT)
		GPIO.setup(self.Motor1B,GPIO.OUT)
		GPIO.setup(self.Motor1E,GPIO.OUT)

	def shoot(self, timeForward,timeBackward):
		print 'Turning motor forward'
		self.turnForwardForTime(timeForward)
		#sleep(1)
		#print 'Turning motor backward'
		#self.turnReverseForTime(timeBackward)
	
	def turnForwardForTime(self,timeAmount):
		self.turnOnForward()
		sleep(timeAmount)
		self.turnOff()

	def turnReverseForTime(self, timeAmount):
		self.turnOnReverse()
		sleep(timeAmount)
		self.turnOff()

	def turnOnForward(self): 
		GPIO.output(self.Motor1A, GPIO.HIGH)
		GPIO.output(self.Motor1B, GPIO.LOW)
		GPIO.output(self.Motor1E, GPIO.HIGH)
	
	def turnOnReverse(self):
		GPIO.output(self.Motor1A, GPIO.LOW)
		GPIO.output(self.Motor1B, GPIO.HIGH)
		GPIO.output(self.Motor1E, GPIO.HIGH)

	def turnOff(self):
		print 'Stopping motor'
		GPIO.output(self.Motor1E,GPIO.LOW)

	def __del__(self):
		GPIO.cleanup()


_motorControl = motorControl()

#GPIO.cleanup()

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('144.39.210.100',50000))

print sock.getsockname()

keepGoing = True
while keepGoing:
	print 'I\'m listening...'
	data, addr = sock.recvfrom(1024)

	if data == 'shoot': 
		_motorControl.shoot(2,1.5)
	elif data == 'exit':
		keepGoing = False

	print 'I got: ' + data

GPIO.cleanup()
