import RPi.GPIO as GPIO
import time

class LedDriver(object) :
    def __init__(self, channel):
        self.channel = channel
        GPIO.setup(self.channel, GPIO.OUT)

    def turnOn(self):
        GPIO.output(self.channel, 1)

    def turnOff(self):
        GPIO.output(self.channel, 0)

    def destroy(self):
        self.turnOff(self)
