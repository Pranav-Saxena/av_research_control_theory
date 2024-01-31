from vehicle import Driver
from controller import Keyboard
from controller import GPS
driver = Driver()
keyboard = Keyboard()
gps=GPS('gps')

sampling=40
Kp=2
K1=0.2
Kd=0.1
init=gps.getValues()[0]
target=-77
map=target-init
gps.enable(sampling)

# driver.setBrakeIntensity(0)
while driver.step() != -1:
    
    x=gps.getValues()[0]
    v=Kp*(target-x)
    # driver.setBrakeIntensity(1-(v/map))
    driver.setCruisingSpeed(abs(v))
    
    print(x)
 
