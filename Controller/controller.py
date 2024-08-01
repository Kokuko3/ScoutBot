from bluedot import Bluedot
from signal import pause
import time
import board
from adafruit_motorkit import MotorKit

def set_speed_right(pos):
    speed = pos.y
    kit.motor1.throttle = speed

def set_speed_left(pos):
    speed = pos.y
    kit.motor4.throttle = speed

kit = MotorKit(i2c=board.I2C())
bd = Bluedot(rows=1,col=2)

bd[0,0].when_moved = set_speed_left
bd[1,0].when_moved = set_speed_right

pause()

kit.motor1.throttle = 0
kit.motor4.throttle = 0