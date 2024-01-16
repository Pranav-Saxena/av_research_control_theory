from vehicle import Driver
from controller import Keyboard
driver = Driver()
keyboard = Keyboard()

while driver.step() != -1:
    key = keyboard.getKey()
    if(key == ord('W')):
        driver.setCruisingSpeed(5)
        driver.setBrakeIntensity(0)
        driver.setSteeringAngle(0)
        driver.setGear(1)
        if driver.getCurrentSpeed()>10:
            driver.setThrottle(0.2)
        elif driver.getCurrentSpeed()>30:
            driver.setThrottle(0)
        else:
            driver.setThrottle(0.4)
        
        
    elif(key == ord('S')):
        driver.setBrakeIntensity(0)
        driver.setSteeringAngle(0)
        driver.setCruisingSpeed(-5)
        driver.setGear(-1)
        if driver.getCurrentSpeed()>10:
            driver.setThrottle(0.2)
        elif driver.getCurrentSpeed()>30:
            driver.setThrottle(0)
        else:
            driver.setThrottle(0.4)
    elif(key == ord('X')):
        driver.setThrottle(0)
        driver.setBrakeIntensity(1)
    elif(key == ord('A')):
        driver.setSteeringAngle(-0.15)
 
    elif(key == ord('D')):
        driver.setSteeringAngle(0.15)
    else:
        pass