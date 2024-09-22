# import libraries needed
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# read data from files
list_1_001 = []
list_1_002 = []
list_1_003 = []
list_1_0005 = []
list_1_0018 = []
list_5_001 = []
list_5_002 = []
list_5_003 = []
list_5_0005 = []
list_5_0018 = []

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case1_0.01.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_1_001.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case1_0.02.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_1_002.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case1_0.03.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_1_003.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case1_0.018.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_1_0018.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case1_0.005.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_1_0005.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case5_0.01.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_5_001.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case5_0.02.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_5_002.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case5_0.03.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_5_003.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case5_0.018.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_5_0018.append([float(line_1),float(line_2),float(line_3)])

with open('E:\Cam_academic\Second year\Mars-lander project\Assignment-4\Lander\Lander\data_case5_0.005.txt', 'r') as file:
    while True:
        line_1 = file.readline().strip()
        if not line_1:
            break
        line_2 = file.readline().strip()
        line_3 = file.readline().strip()
        list_5_0005.append([float(line_1),float(line_2),float(line_3)])


scenario = 1
k_h = 0.018
# Create the figure and axis
fig = plt.figure(figsize=(12, 6))
ax = fig.add_subplot(1,1,1)
plt.subplots_adjust(left=0.2, bottom=0.35)# Leave space for textbox
#  Add legend
ax.legend(loc='upper right')
# Set labels
ax.set_xlabel('altitude')
ax.set_ylabel('descent rate')
ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')    
Real, = ax.plot(np.array(list_1_0018)[:,0],np.array(list_1_0018)[:,1], color='blue',label = "Actual descent rate")
Ideal, = ax.plot(np.array(list_1_0018)[:,0],np.array(list_1_0018)[:,2], color='red',label = "Ideal descent rate")
plt.text(-0.2, -0.4, 'scenario 1: descent from 10km', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5),transform=plt.gca().transAxes)
plt.text(-0.2, -0.5, 'scenario 5: descent from 200km', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5),transform=plt.gca().transAxes)
# Create textbox
button_ax_s1 = plt.axes([0.3, 0.05, 0.2, 0.075])
button_s1 = Button(button_ax_s1, f'scenario 1')
button_ax_s5 = plt.axes([0.6, 0.05, 0.2, 0.075])
button_s5 = Button(button_ax_s5, f'scenario 5')
button_ax_k0005 = plt.axes([0.1, 0.2, 0.1, 0.075])
button_k0005 = Button(button_ax_k0005, f'k_h = 0.005')
button_ax_k001 = plt.axes([0.25, 0.2, 0.1, 0.075])
button_k001 = Button(button_ax_k001, f'k_h = 0.01')
button_ax_k0018 = plt.axes([0.4, 0.2, 0.1, 0.075])
button_k0018 = Button(button_ax_k0018, f'k_h = 0.018')
button_ax_k002 = plt.axes([0.55, 0.2, 0.1, 0.075])
button_k002 = Button(button_ax_k002, f'k_h = 0.02')
button_ax_k003 = plt.axes([0.7, 0.2, 0.1, 0.075])
button_k003 = Button(button_ax_k003, f'k_h = 0.03')

# when button is clicked
def on_button_click(event,label):
    global scenario,k_h
    if label == "s1":
        scenario = 1
    if label == "s5":
        scenario = 5
    if label == "k0005":
        k_h = 0.005
    if label == "k001":
        k_h = 0.01
    if label == "k0018":
        k_h = 0.018
    if label == "k002":
        k_h = 0.02
    if label == "k003":
        k_h = 0.03
    if scenario == 1:
        if k_h == 0.005:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_1_0005)[:,0])
            Real.set_ydata(np.array(list_1_0005)[:,1])
            Ideal.set_xdata(np.array(list_1_0005)[:,0])
            Ideal.set_ydata(np.array(list_1_0005)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.01:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_1_001)[:,0])
            Real.set_ydata(np.array(list_1_001)[:,1])
            Ideal.set_xdata(np.array(list_1_001)[:,0])
            Ideal.set_ydata(np.array(list_1_001)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.018:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_1_0018)[:,0])
            Real.set_ydata(np.array(list_1_0018)[:,1])
            Ideal.set_xdata(np.array(list_1_0018)[:,0])
            Ideal.set_ydata(np.array(list_1_0018)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.02:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_1_002)[:,0])
            Real.set_ydata(np.array(list_1_002)[:,1])
            Ideal.set_xdata(np.array(list_1_002)[:,0])
            Ideal.set_ydata(np.array(list_1_002)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.03:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_1_003)[:,0])
            Real.set_ydata(np.array(list_1_003)[:,1])
            Ideal.set_xdata(np.array(list_1_003)[:,0])
            Ideal.set_ydata(np.array(list_1_003)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
    else:
        if k_h == 0.005:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_5_0005)[:,0])
            Real.set_ydata(np.array(list_5_0005)[:,1])
            Ideal.set_xdata(np.array(list_5_0005)[:,0])
            Ideal.set_ydata(np.array(list_5_0005)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.01:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_5_001)[:,0])
            Real.set_ydata(np.array(list_5_001)[:,1])
            Ideal.set_xdata(np.array(list_5_001)[:,0])
            Ideal.set_ydata(np.array(list_5_001)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.018:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_5_0018)[:,0])
            Real.set_ydata(np.array(list_5_0018)[:,1])
            Ideal.set_xdata(np.array(list_5_0018)[:,0])
            Ideal.set_ydata(np.array(list_5_0018)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.02:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_5_002)[:,0])
            Real.set_ydata(np.array(list_5_002)[:,1])
            Ideal.set_xdata(np.array(list_5_002)[:,0])
            Ideal.set_ydata(np.array(list_5_002)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()
        if k_h == 0.03:
            ax.set_title(f'descent rate against altitude with K_h = {k_h} in  scenario {scenario}')
            Real.set_xdata(np.array(list_5_003)[:,0])
            Real.set_ydata(np.array(list_5_003)[:,1])
            Ideal.set_xdata(np.array(list_5_003)[:,0])
            Ideal.set_ydata(np.array(list_5_003)[:,2])
            ax.relim()  # reshape graph
            ax.autoscale_view() 
            ax.legend()
            plt.draw()



button_s1.on_clicked(lambda event: on_button_click(event, "s1"))
button_s5.on_clicked(lambda event: on_button_click(event, "s5"))
button_k0005.on_clicked(lambda event: on_button_click(event, "k0005"))
button_k001.on_clicked(lambda event: on_button_click(event, "k001"))
button_k0018.on_clicked(lambda event: on_button_click(event, "k0018"))
button_k002.on_clicked(lambda event: on_button_click(event, "k002"))
button_k003.on_clicked(lambda event: on_button_click(event, "k003"))
ax.relim()  # reshape graph
ax.autoscale_view() 
plt.show()




