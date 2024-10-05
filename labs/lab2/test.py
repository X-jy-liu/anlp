import numpy as np
print(np.array([1,2,3]))
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create a figure and axis
fig, ax = plt.subplots()

# Plot data
ax.plot(x, y, label='Linear Growth', marker='o')

# Add a title and labels
ax.set_title('Simple Line Plot')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')

# Add a grid
ax.grid(True)

# Add a legend
ax.legend()

# Show the plot
plt.show()