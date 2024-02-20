import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def simulate_collision(mass1, velocity1, mass2, velocity2, elasticity, duration, time_step):
    positions1 = [0]   # initial position of the first object
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
    mass1_val = slider_mass1.val
    velocity1_val = slider_velocity1.val
    mass2_val = slider_mass2.val
    velocity2_val = slider_velocity2.val
    elasticity_val = slider_elasticity.val

    positions1, positions2 = simulate_collision(mass1_val, velocity1_val, mass2_val, velocity2_val, elasticity_val, duration, time_step)
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

# Add sliders for mass, velocity, and elasticity
slider_mass1_ax = plt.axes([0.1, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_mass1 = Slider(slider_mass1_ax, 'Mass 1', 0.1, 5.0, valinit=mass1)
slider_mass1.on_changed(update)

slider_velocity1_ax = plt.axes([0.1, 0.06, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_velocity1 = Slider(slider_velocity1_ax, 'Velocity 1', -5.0, 5.0, valinit=velocity1)
slider_velocity1.on_changed(update)

slider_mass2_ax = plt.axes([0.1, 0.11, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_mass2 = Slider(slider_mass2_ax, 'Mass 2', 0.1, 5.0, valinit=mass2)
slider_mass2.on_changed(update)

slider_velocity2_ax = plt.axes([0.1, 0.16, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_velocity2 = Slider(slider_velocity2_ax, 'Velocity 2', -5.0, 5.0, valinit=velocity2)
slider_velocity2.on_changed(update)

slider_elasticity_ax = plt.axes([0.1, 0.21, 0.65, 0.03], facecolor='lightgoldenrodyellow')
slider_elasticity = Slider(slider_elasticity_ax, 'Elasticity', 0.0, 1.0, valinit=elasticity_initial)
slider_elasticity.on_changed(update)

plt.show()
