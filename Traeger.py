import RPi.GPIO as GPIO
import time
import logging
import logging.config

#Start logging
logging.config.fileConfig('/home/pi/pelletpirate/pelletpirate/logging.conf')
logger = logging.getLogger(__name__)


class Traeger:
    def __init__(self, Relays):
        self.Relays = Relays
        self.ToggleTime = {}
        self.Initialize()

    def Initialize(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for k in list(self.Relays.keys()):
            GPIO.setup(self.Relays[k], GPIO.OUT)
            self.SetState(k, 0)
            self.ToggleTime[k] = time.time()

    def GetState(self, Relay):
        return not GPIO.input(self.Relays[Relay])

    def SetState(self, Relay, state):
        if not (self.GetState(Relay) == state):
            logger.info('Toggling %s: %d', Relay, state)
            self.ToggleTime[Relay] = time.time()
        GPIO.output(self.Relays[Relay], not state)

