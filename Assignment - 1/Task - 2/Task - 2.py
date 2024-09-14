# This program aims to compare the performance of both Euler method and Verlet method when dt changes.
# To simplify the graph presented, only displacement(x) is shown.(If x diverges, v will diverge as well and vice versa)

#---------------------------------------------------------------------------------------------------------------------------------
# import libraries needed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

#---------------------------------------------------------------------------------------------------------------------------------
# define Euler integration
def Integration_E(m_E,k_E,dt_E,x_E,v_E,t):
    # m is mass
    # k is stiffness of spring
    # dt is time division
    # x is displacement
    # v is velocity
    # t is maximum time

    m = m_E
    k = k_E
    dt = dt_E
    x = x_E
    v = v_E
    t_max = t
    # initialise empty lists to record trajectories
    x_list = []# ------------------ Y-axis for Euler method
    v_list = []
    t_array = np.arange(0, t_max, dt) # ------------------ X-axis
    # Euler integration
    for t in t_array:

        # append current state to trajectories
        x_list.append(x)
        v_list.append(v)

        # calculate new position and velocity
        a = -k * x / m
        x = x + dt * v
        v = v + dt * a

    # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    x_array = np.array(x_list)
    v_array = np.array(v_list)

    return x_array,v_array,t_array


#---------------------------------------------------------------------------------------------------------------------------------
# define Verlet integration
def Integration_V(m_V,k_V,dt_V,x_V,v_V,t):
    # m is mass
    # k is stiffness of spring
    # dt is time division
    # x is displacement
    # v is velocity
    # t is maximum time
    
    m = m_V
    k = k_V
    dt = dt_V
    x = x_V
    v = v_V
    t_max = t
    # initialise empty lists to record trajectories
    x_list = []# ------------------ Y-axis for Euler method
    v_list = []
    t_array = np.arange(0, t_max, dt) # ------------------ X-axis
    # Verlet integration
    for t in t_array:

        # append current state to trajectories
        x_list.append(x)
        v_list.append(v)

        # calculate new position and velocity
        if t == 0:
            a = - k * x / m
            x = x + dt * v + (dt ** 2) * a
            v = (x - x_list[-1]) / dt
        else:
            a = - k * x / m
            x = 2 * x - x_list[-2]+ (dt ** 2) * a
            v = (x - x_list[-1]) / dt

    # convert trajectory lists into arrays, so they can be sliced (useful for Assignment 2)
    x_array = np.array(x_list)
    v_array = np.array(v_list)

    return x_array,v_array,t_array


#---------------------------------------------------------------------------------------------------------------------------------
# Create the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.2, bottom=0.35)# Leave space for two sliders

# Generate initial data
# mass, spring constant, initial position and velocity, simulation time, timestep and time
t_max = 100
m = 1
k = 1
dt_E = 0.1
dt_V = 0.1
x_E = 0
v_E = 1
x_V = 0
v_V = 1

# Plot both Euler amd verlet method
plt.ylim(-10,10)
t_ana = np.arange(0, t_max, 0.1)
Analytical, = ax.plot(t_ana,np.sin(t_ana), label="Analytical method",color = 'green')
Euler, = ax.plot(Integration_E(m,k,dt_E,x_E,v_E,t_max)[2],Integration_E(m,k,dt_E,x_E,v_E,t_max)[0], label="Euler method")
Verlet, = ax.plot(Integration_E(m,k,dt_E,x_E,v_E,t_max)[2],Integration_V(m,k,dt_V,x_V,v_V,t_max)[0], label="Verlet method", color='orange')

# Add legend
ax.legend()

# Set labels
ax.set_xlabel('time')
ax.set_ylabel('displacement')
ax.set_title('displacement of spring-mass system for Euler and Verlet method')

# Create sliders for both Euler amd verlet method
ax_slider_E = plt.axes([0.1, 0.2, 0.8, 0.05], facecolor='lightgoldenrodyellow')  # dt for Euler method slider
ax_slider_V = plt.axes([0.1, 0.1, 0.8, 0.05], facecolor='lightcoral')  # dt for Verlet method slider


slider_E = Slider(ax_slider_E, 'Euler', 0.001, 10.0, valinit=dt_E)
slider_V = Slider(ax_slider_V, 'Verlet', 0.001, 10.0, valinit=dt_V)

# Update function for both sliders
def update(val):
    # Generate initial data
    # mass, spring constant, initial position and velocity,simulation time, timestep and time
    global m,k,x_E,x_V,v_E,v_V,t_max
    dt_E = slider_E.val  # Get the dt from the first slider
    dt_V = slider_V.val  # Get the dt from the second slider
    Euler.set_xdata(Integration_E(m,k,dt_E,x_E,v_E,t_max)[2])  # Update t_Euler
    Euler.set_ydata(Integration_E(m,k,dt_E,x_E,v_E,t_max)[0])  # Update x_Euler
    Verlet.set_xdata(Integration_V(m,k,dt_V,x_V,v_V,t_max)[2])  # Update t_Verlet
    Verlet.set_ydata(Integration_V(m,k,dt_V,x_V,v_V,t_max)[0])  # Update x_Verlet
    fig.canvas.draw_idle()  # Redraw the plot

# Connect sliders to the update function
slider_E.on_changed(update)
slider_V.on_changed(update)

plt.show()