# This program aims to compare movement of an object in the gravitational field of a planet when initial velocity changes.
# Slider is added so that initial velocity can be changed manually.
# The integration in this program is based on Verlet method.

#---------------------------------------------------------------------------------------------------------------------------------
# import libraries needed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
from matplotlib.patches import Circle
import math 


#---------------------------------------------------------------------------------------------------------------------------------
# define a function to calculate vector of force and velocity
def force(G,M,m,x):
    # modulous is length of x
    modulous = np.linalg.norm(x)
    unitv = x / modulous
    f = - unitv * ((G * M * m) / (modulous ** 2))
    return f

def velocity(v):
    return np.array([1,0,0]) * v

#---------------------------------------------------------------------------------------------------------------------------------
# define Verlet integration
def Integration_E(G,M,m,h,v,t_max,dt):
    # G is gravitational constant
    # M is mass of planet
    # m is mass of object though it is useless as mass of object does not matter movement
    # x is height of object
    # v is 3-D velocity of object

    G = G
    M = M
    m = m
    r = np.array([0,1,0])*3.39e6
    x = h + r
    v = velocity(v)
    t_max = t_max
    dt = dt

    # initialise empty lists to record trajectories
    x_list = []
    t_array = np.arange(0,t_max, dt) # ------------------ X-axis
    # Verlet integration
    for t in t_array:
        # detect if the satellite has touched mars
        modulous = np.linalg.norm(x)
        if modulous <= 3.39e6:
            x_list.append(x)
            break

        # append current state to trajectories
        x_list.append(x)

        # calculate new position and velocity
        if t == 0:
            a = force(G,M,m,x) / m
            x = x + dt * v + (dt ** 2) * a
            v = (x - x_list[-1]) / dt
        else:
            a = force(G,M,m,x) / m
            x = 2 * x - x_list[-2]+ (dt ** 2) * a
            v = (x - x_list[-1]) / dt
        
        # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    x_array = np.array(x_list)
    return x_array
    
#---------------------------------------------------------------------------------------------------------------------------------
# Create the figure and axis
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1,1,1)
plt.subplots_adjust(left=0.2, bottom=0.35)# Leave space for textbox

# Generate initial data
# mass, spring constant, initial position and velocity, simulation time, timestep and time
t_max = 30000
m = 1000
dt = 0.1
r = np.array([0,1,0])*3.39e6
G = 6.6743e-11
M = 6.42e23
h = np.array([0,1,0])*3.39e6 # height above surface of mars
v  = 0

# Plot graph
x_array = Integration_E(G,M,m,h,v,t_max,dt)
Verlet, = ax.plot(x_array[:,0],x_array[:,1], color='blue')

#  Add legend
ax.legend()
# Set labels
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('movement of satellite based on different initial speed - verlet')    
orbital_s = fig.text(0.7, 0.8, f'Orbital spped: {math.sqrt(G*M/np.linalg.norm((h+r)))} m/s', fontsize=12, color='black')
escape_s = fig.text(0.7, 0.7, f'Escape speed: {math.sqrt(2*G*M/np.linalg.norm((h+r)))} m/s', fontsize=12, color='black')

# Create textbox
speed = plt.axes([0.3, 0.05, 0.6, 0.075])  # position of textbox
height = plt.axes([0.3, 0.15, 0.6, 0.075])
text_box_S = TextBox(speed, 'Initial velocity (m/s): ', initial="0")
text_box_H = TextBox(height, 'Height above surface (m): ', initial="3.39e6")
# Update function for textbox
def submit(speed,height):
    global t_max,m,dt,G,M,r
    h = np.array([0,1,0])*float(height)
    v = float(speed)
    data = Integration_E(G,M,m,h,v,t_max,dt)
    Verlet.set_xdata(data[:,0])
    Verlet.set_ydata(data[:,1])
    orbital_s.set_text( f'Orbital spped: {math.sqrt(G*M/np.linalg.norm((h+r)))} m/s')
    escape_s.set_text( f'Escape speed: {math.sqrt(2*G*M/np.linalg.norm((h+r)))} m/s')
    ax.relim()  # reshape graph
    ax.autoscale_view() 
    plt.draw()

# Connect textbox to the update function
def submit_all(text):
    submit(text_box_S.text, text_box_H.text)
text_box_S.on_submit(submit_all) 
text_box_H.on_submit(submit_all) 
c = Circle(xy=(0, 0), radius=3.39e6, alpha=0.5, color='red')  # circle
ax.add_patch(c)
plt.text(-0.4, 9, 'Red ball is Mars', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
plt.text(-0.4, 8, 'Blue curve is trajectory of satellite', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
plt.text(-0.4, 7, 'Gravitational constant:6.6743e-11', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
plt.text(-0.4, 6, 'Mass of Mars:6.42e23 kg', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
plt.text(-0.4, 5, 'Mass of satellite:1000 kg', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
plt.text(-0.4, 4, 'Radius of Mars:3.39e6 m', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))


ax.set_aspect('equal')
plt.show()

