"""
Author: Aneesh Bulusu and Smarth Gupta
Date: March 22 2020
Description: An Euler method simulation of a steel ball bearing being dropped into a 
tube of canola oil with infinite radius and infinite depth. 
Example running command:t2.py
"""
  
import matplotlib.pyplot as plt

#Constants		    
pi = 3.14159265358979323846 #pi
r = 0.0075                  #radius of the ball bearing
rho = 7850                  #density of steel (kg/m^3)
sigma = 910                 #density of canola oil at room temp (kg/m^3)
eta = 0.0635                 #viscosity of canola oil (Pa*s) 
g = 9.81                    #acceleration due to gravity (m/s^2) 
m = 4/3*pi*r**3*rho         #mass of the object (kg) 

#Choose initial conditions and time step for Euler method
t = 0
dt = 0.001
x = 0
v = 0


#Initialize lists for plotting
time = []
position = []
velocity = []


while x < 0.3:
	v = v + (4/3*pi*r**3*g*(rho-sigma)-6*pi*eta*r*v)/m*dt
	x = x + v*dt
	t = t + dt
	

	time.append(t)
	position.append(x)
	velocity.append(v)
	#acceleration.append(a)

print(v)
print(velocity)


plt.plot(time, velocity, "b.")
plt.title("Velocity versus Time (Python Model)")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")

plt.grid(True)
plt.show()
