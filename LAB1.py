# %% [markdown]
# Part 1: Review concepts about the point robot
# 
# Test your simulator with a line trajectory and a circular trajectory.
# 
# 
# 

# %%
%pylab inline

# %%
# Perfect sensor
def sense(x):
    return x

# %%
def simulate(Δt, x, u):
    x += Δt * u
    return x

# %%
def line_control(t, y):
    ### WRITE YOUR CONTROL POLICY HERE:
    ux = 2
    uy = 1
    return array([ux, uy])

# %%
tf = 3.
Δt = 0.1    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval


# Initial conditions
x = array([2., 1.])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = line_control(t, y)    
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)

# %%
grid()
plot(x_log[:,0], x_log[:,1])

# %%
def circle_control(t, y):
    ### WRITE YOUR CONTROL POLICY HERE:
    ux = -sin(t)
    uy = cos(t)
    return array([ux, uy])

# %%
tf = 2 * pi
Δt = 0.1    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval


# Initial conditions
x = array([2., 1.])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = circle_control(t, y)    
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)

# %%
plt.axis('equal') 
grid()
plot(x_log[:,0], x_log[:,1])

# %% [markdown]
# Part 2: Design a controller to follow an elliptical trajectory (Chapter 2)
# 
# Answer the following exercises, depending on the course:
# 
# Exercises 1, 3 for CSE360 students​ (exercise 2 is optional).
# Exercises 1,2, and 3 for 460 students
# 

# %%
def elliptical1_control(t, y):
    ### WRITE YOUR CONTROL POLICY HERE:
    # major axis
    a = 4
    # minor axis
    b = 2
    ux = -a * sin(t)
    uy = b * cos(t)
    return array([ux, uy])


# %%
tf = 2 * pi
Δt = 0.1    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval


# Initial conditions
x = array([7., 2.])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = elliptical1_control(t, y)    
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)

# %%
plt.axis('equal')
grid()
plot(x_log[:,0], x_log[:,1])

# %%
def elliptical2_control(t, y):
    ### WRITE YOUR CONTROL POLICY HERE:
    # major axis
    a = 4
    # minor axis
    b = 2
    theta = pi / 6
    c, s = cos(theta), sin(theta)
    R = array([[c, -s], [s, c]])
    
    ux = -a * sin(t)
    uy = b * cos(t)
    ux_rotated, uy_rotated = R.dot(array([ux, uy]))
    
    return array([ux_rotated, uy_rotated])

# %%
tf = 2 * pi
Δt = 0.1    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval


# Initial conditions
x = array([7., 2.])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = elliptical2_control(t, y)    
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)

# %%
plt.axis('equal')
grid()
plot(x_log[:,0], x_log[:,1])

# %%
def eight_curve_control(t, y):
    # Calculate the derivatives of the parametric equations for a standard lemniscate
    a = 1
    b = 2
    
    denom = (1 + sin(t)**2)**2
    
    ux = - a * sin(t) * (sin(t)**2 + 2 * cos(t)**2 + 1) / denom 
    uy = b * (sin(t)**4 + (cos(t)**2 + 1) * sin(t)**2 - cos(t)**2) / denom 

    return array([ux, uy])

# %%
tf = 2 * pi
Δt = 0.01    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval


# Initial conditions
x = array([1., 0.])
x_log = [copy(x)]

for t in time:
    y = sense(x)
    u = eight_curve_control(t, y)    
    x = simulate(Δt, x, u)
    x_log.append(copy(x))
    
x_log = array(x_log)

# %%
plt.axis('equal')
grid()
plot(x_log[:,0], x_log[:,1])

# %%
import matplotlib.pyplot as plt
from matplotlib import animation
from JSAnimation import IPython_display    
from IPython.display import HTML
    
fig, ax = plt.subplots()

def animate(t):
    ax.clear()
    
    # Path
    plot(x_log[:,0], x_log[:,1], 'r--')
    
    # Initial conditions
    plot(x_log[t,0], x_log[t,1], 'bo')
    
    

anim = animation.FuncAnimation(fig, animate, frames=len(time), interval=60)

HTML(anim.to_jshtml())

# %% [markdown]
# Part 3: Simulate windy conditions (Chapter 2)
# Solve Excercise 4 for both wind conditions.

# %% [markdown]
# - Add a constant wind w = [0.1, 0.1]⊤.
# - Add a random wind with mean zero in x and y direction, and standard deviation of 0.1.

# %%
def simulate_wind(Δt, x, u, wind):
    x += Δt * u + wind
    return x

# %%
def circle_control(t, y):
    ### WRITE YOUR CONTROL POLICY HERE:
    ux = -sin(t)
    uy = cos(t)
    return array([ux, uy])

# %%
tf = 2 * pi
Δt = 0.01    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval


# Initial conditions
x = array([1., 0.])
x_log = [copy(x)]
constant_wind = array([0.1, 0.1]) 

for t in time:
    y = sense(x)
    u = circle_control(t, y)    
    x = simulate_wind(Δt, x, u, constant_wind * Δt)
    x_log.append(copy(x))
    
x_log = array(x_log)

# %%
plt.axis('equal')
grid()
plot(x_log[:,0], x_log[:,1])

# %%
import matplotlib.pyplot as plt
from matplotlib import animation
from JSAnimation import IPython_display    
from IPython.display import HTML
    
fig, ax = plt.subplots()

def animate(t):
    ax.clear()
    
    # Path
    plot(x_log[:,0], x_log[:,1], 'r--')
    
    # Initial conditions
    plot(x_log[t,0], x_log[t,1], 'bo')
    
    

anim = animation.FuncAnimation(fig, animate, frames=len(time), interval=60)

HTML(anim.to_jshtml())

# %%
import numpy as np
def simulate_random_wind(Δt, x, u, wind):
    random_wind = random.normal(0,0.1,2)
    x += Δt * u + random_wind
    return x

# %%
tf = 2 * pi
Δt = 0.01    # Time step
time = linspace(0.,tf, int(tf / Δt) + 1)  # Time interval


# Initial conditions
x = array([1., 0.])
x_log = [copy(x)]
random_wind = array([0.1, 0.1]) 

for t in time:
    y = sense(x)
    u = circle_control(t, y)    
    x = simulate_random_wind(Δt, x, u, random_wind * Δt)
    x_log.append(copy(x))
    
x_log = array(x_log)

# %%
plt.axis('equal')
grid()
plot(x_log[:,0], x_log[:,1])

# %%
import matplotlib.pyplot as plt
from matplotlib import animation
from JSAnimation import IPython_display    
from IPython.display import HTML
    
fig, ax = plt.subplots()

def animate(t):
    ax.clear()
    
    # Path
    plot(x_log[:,0], x_log[:,1], 'r--')
    
    # Initial conditions
    plot(x_log[t,0], x_log[t,1], 'bo')
    
    

anim = animation.FuncAnimation(fig, animate, frames=len(time), interval=60)

HTML(anim.to_jshtml())


