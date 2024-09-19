import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

line, = ax.plot(x, y)

# Define the update function for animation
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Shift the sine wave by frame
    return line,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 100, 1), interval=50, blit=True)

plt.show()
