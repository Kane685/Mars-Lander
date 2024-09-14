# uncomment the next line if running in a notebook
# %matplotlib inline
import numpy as np
import time
# import matplotlib.pyplot as plt

def time_test(dt):
    # start time
    start_time = time.perf_counter()
    # mass, spring constant, initial position and velocity
    m = 1
    k = 1
    x = 0
    v = 1

    # simulation time, timestep and time
    t_max = 100
    t_array = np.arange(0, t_max, dt)

    # initialise empty lists to record trajectories
    x_list = []
    v_list = []
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
    # end time
    end_time = time.perf_counter()
    # calculate time consumed and print 
    elapsed_time = end_time - start_time
    print(f"Execution time - Euler: {elapsed_time} second when dt is : {dt}")
# # plot the position-time graph
# plt.figure(1)
# plt.clf()
# plt.xlabel('time (s)')
# plt.grid()
# plt.plot(t_array, x_array, label='x (m)')
# plt.plot(t_array, v_array, label='v (m/s)')
# plt.legend()
# plt.show()

time_list = [0.1,0.01,0.001,0.0001,0.00001]
for i in time_list:
    time_test(i)