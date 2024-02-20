import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from matplotlib.widgets import Slider

# Constants
mass = 1.0
spring_constant = 10.0
initial_displacement = 1.0
initial_velocity = 0.0

# Function representing the system of ODEs for the spring-mass system
def system(t, state, damping_factor):
    position, velocity = state
    acceleration = -spring_constant / mass * position - damping_factor * velocity
    return [velocity, acceleration]

# Initial conditions
initial_state = [initial_displacement, initial_velocity]

# Time span for the simulation
t_span = (0, 10)

# Create a figure and axis for the plot
fig, ax = plt.subplots(figsize=(8, 6))
plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9)

# Solve the system of ODEs using solve_ivp
def solve_system(damping_factor):
    solution = solve_ivp(system, t_span, initial_state, args=(damping_factor,), t_eval=np.linspace(t_span[0], t_span[1], 1000))
    positions = solution.y[0]
    velocities = solution.y[1]
    return solution.t, positions, velocities

# Plot the results
def plot_results(damping_factor):
    t, positions, velocities = solve_system(damping_factor)
    ax.clear()
    ax.plot(t, positions, label='Position')
    ax.plot(t, velocities, label='Velocity')
    ax.set_title('Spring-Mass System - Simple Harmonic Motion')
    ax.set_xlabel('Time')
    ax.set_ylabel('Amplitude')
    ax.legend()
    ax.grid(True)

# Add damping factor slider
slider_ax = plt.axes([0.1, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
damping_factor_slider = Slider(slider_ax, 'Damping Factor', 0.0, 1.0, valinit=0.2)

# Update function for the slider
def update(val):
    damping_factor = damping_factor_slider.val
    plot_results(damping_factor)
    fig.canvas.draw_idle()

# Attach the update function to the slider
damping_factor_slider.on_changed(update)

# Initial plot
plot_results(initial_displacement)

plt.show()
