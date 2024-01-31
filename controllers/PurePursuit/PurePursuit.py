from vehicle import Driver
from controller import GPS
from math import sin,atan2,hypot
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

# variables
time_step=40
# create the Robot instance.
driver = Driver()

gpsr=GPS('gpsr')
gpsr.enable(time_step)

gpsf=GPS('gpsf')
gpsf.enable(time_step)

class PurePursuit():
    def __init__(self, path, look_ahead, lin,current=[0,0]):
        self.path = path
        self.current = current
        self.target=[0,0]
        self.lookahead = look_ahead
        self.linear = lin
        self.nearest=0
        self.WB=3.5
    #calculates distance between 2 points and inclination of resulting line
    def getParams(self,point1, point2):
       x_diff = point2[0] - point1[0]
       y_diff = point2[1] - point1[1]
       angle =atan2(y_diff, x_diff)
       dist=hypot(y_diff,x_diff)
       return [dist, angle]

    #updates target point using look_ahead distance
    def setTarget(self):
        try:
            self.nearest = self.indexOfClosestPoint(self.path, 0, self.current)
            self.path=self.path[self.nearest:]
            targetIndex = self.indexOfClosestPoint(self.path[self.nearest:], self.lookahead, self.current)
            self.target=self.path[targetIndex]
            print(self.current[0],self.current[1])

        except IndexError:
            self.linear=0
            self.WB=0

        

        

    @staticmethod
    def indexOfClosestPoint(points, radius, target_point):
        #find index of point in list with least abs(distance to target point- radius)
        
        index_least = 0
        min_difference = abs(hypot(points[0][0] - target_point[0], points[0][1] - target_point[1]) - radius)

        for i in range(1, len(points)):
            dist = hypot(points[i][0] - target_point[0], points[i][1] - target_point[1])
            current_difference = abs(dist - radius)

            if current_difference < min_difference:
                min_difference = current_difference
                index_least = i

        return index_least
        

    def steeringAngle(self,yaw):
        self.setTarget()
        target_yaw = self.getParams(self.current, self.target)[1]
        steer = np.arctan2(self.WB*2*sin(target_yaw - yaw)/self.lookahead,1.0)
        return steer



myposes=[[-45,45],[-60,45],[-85,38.7],[-92,33],[-105,4.5],[-105,-15],[-105,-35],[-105,-50],[-102,-78],[-91,-94],[-64.5,-105],[-35,-105],[-10,-105],[33,-93],[45,-65],[45,-45],[45,4.5],[45,-20],[45,-10],[45,10],[36,30],[17,42],[-5,45],[-30,45]]

purepursuit = PurePursuit(myposes, 25, 65,[gpsr.getValues()[0],gpsr.getValues()[1]])

# - perform simulation steps until Webots is stopping the controller
x=[]
y=[]
while driver.step() != -1:
    x_del = gpsf.getValues()[0] - gpsr.getValues()[0]
    y_del = gpsf.getValues()[1] - gpsr.getValues()[1]
    x.append(gpsr.getValues()[0])
    y.append(gpsr.getValues()[1])
    yaw =atan2(y_del, x_del)

    purepursuit.current = [gpsr.getValues()[0], gpsr.getValues()[1]]
    driver.setCruisingSpeed(purepursuit.linear)
    angle = purepursuit.steeringAngle(yaw)
    driver.setSteeringAngle(-angle)
    if driver.getCurrentSpeed()<0.02:
        x_values, y_values = zip(*myposes)

        # Plot the points
        plt.plot(x_values, y_values,'ro-', label='Given Path')
        plt.title('trajectory Plots')
        plt.xlabel('X[m]')
        plt.ylabel('Y[m]')
        plt.plot(x, y,'b--',label='Traversed Path')
        plt.legend()
    
        plt.show()
      


    
    

