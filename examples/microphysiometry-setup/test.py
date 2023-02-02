from openworkstation import robot2
from moduleSensor import *
from moduleLifter import *
from moduleTransportation import *
from commands import *

robot2.reset()

connect()

#move_to_lidHolder()
#move_to_moduleLifter()
robot2._driver.send_command('G90')
robot2._driver.send_command('G0 F20000')
robot2._driver.send_command('G0 X100 Y-200 Z3')