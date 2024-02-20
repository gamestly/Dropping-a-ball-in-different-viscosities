import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulate_collision(mass1, velocity1, mass2, velocity2, elasticity, duration, time_step):
    positions1 = [0]
    positions2 = [10]  # Initial position of the second object

    for _ in range(int(duration / time_step)):
        # Update positions
        positions1.append(positions1[-1] + velocity1 * time_step)
        positions2.append(positions2[-1] + velocity2 * time_step)

        # Check for collision
        if positions1[-1] >= positions2[-1]:
            # Perform collision
            v1_f = ((mass1 - elasticity * mass2) * velocity1 + (1 + elasticity) * mass2 * velocity2) / (mass1 + mass2)
            v2_f = ((mass2 - elasticity * mass1) * velocity2 + (1 + elasticity) * mass1 * velocity1) / (mass1 + mass2)

            # Update velocities after collision
            velocity1 = v1_f
            velocity2 = v2_f

    return positions1, positions2

def update(val):
    elasticity = slider.val
    positions1, positions2 = simulate_collision(mass1, velocity1, mass2, velocity2, elasticity, duration, time_step)
    line1.set_ydata(positions1)
    line2.set_ydata(positions2)
    fig.canvas.draw_idle()

# Simulation parameters
mass1 = 1.0
velocity1 = 2.0
mass2 = 1.0
velocity2 = -1.0
elasticity_initial = 0.8
duration = 5.0
time_step = 0.01

# Initial simulation
positions1, positions2 = simulate_collision(mass1, velocity1, mass2, velocity2, elasticity_initial, duration, time_step)

# Plot the results
fig, ax = plt.subplots()
line1, = ax.plot(positions1, label='Object 1')
line2, = ax.plot(positions2, label='Object 2')
ax.set_xlabel('Time')
ax.set_ylabel('Position')
ax.legend()
ax.set_title('1D Head-on Collision Simulation')

# Add coefficient of restitution slider
slider_ax = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider = Slider(slider_ax, 'Elasticity', 0.0, 1.0, valinit=elasticity_initial)

# Update function for the slider
def update(val):
    elasticity = slider.val
    positions1, positions2 = simulate_collision(mass1, velocity1, mass2, velocity2, elasticity, duration, time_step)
    line1.set_ydata(positions1)
    line2.set_ydata(positions2)
    fig.canvas.draw_idle()

slider.on_changed(update)

plt.show()
