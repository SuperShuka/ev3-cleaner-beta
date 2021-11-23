#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.



# Create your objects here.

ev3 = EV3Brick()
ev3.speaker.beep()

left_motor = Motor(Port.A)
right_motor = Motor(Port.D)
lwash = Motor(Port.B)
rwash = Motor(Port.C)
fsens = UltrasonicSensor(Port.S1)
lsens = UltrasonicSensor(Port.S4)

ev3.screen.set_font(family=None, size=64, bold=True, monospace=False, lang='en', script=None)
robot = DriveBase(left_motor, right_motor, wheel_diameter=70, axle_track=104)

walls = 0
room = list()
degree = 0

# Write your program here.

ev3.screen.print(walls)
lwash.run(1000)
rwash.run(1000)
ev3.speaker.play_file('secret.wav')

while (not(Button.CENTER in ev3.buttons.pressed())):
    if (Button.LEFT in ev3.buttons.pressed()):
        walls-=1
        ev3.screen.print(walls)
        wait(250)
    if (Button.RIGHT in ev3.buttons.pressed()):
        walls+=1
        ev3.screen.print(walls)
        wait(250)

robot.drive(200, 0)
while fsens.distance(True) > 50:
    wait(10)
robot.stop
