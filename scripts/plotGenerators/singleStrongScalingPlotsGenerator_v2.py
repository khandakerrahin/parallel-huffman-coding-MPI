import matplotlib.pyplot as plt
import numpy as np

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]
times = [4.211, 2.2351, 1.5485000000000002, 1.8893, 2.4956, 3.7978999999999994, 2.3634999999999997, 5.2963000000000005]

times = [time * 1000 for time in times] # convert time to milliseconds

# Plot the ideal case of linear scaling
plt.plot(num_procs, [times[0] / p for p, t in zip(num_procs, times)], linewidth=5, color='red', label='Ideal scaling')
plt.plot(num_procs, times, linewidth=5, label='Result scaling')
plt.xlabel('Number of Processors')
plt.xscale('log', base=10)
plt.yscale('log', base=10)
plt.ylabel('Processing Time (ms)')
plt.title('Strong Scaling: 6.5MB file')
plt.plot(1, 1000000)
plt.plot(100, 1000000)
# Add a legend
plt.grid(True, linestyle='-', alpha=0.7)
plt.legend()

# Set origin to (1,1)
ax = plt.gca()
ax.spines['left'].set_position(('data', 1))
ax.spines['bottom'].set_position(('data', 1))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

plt.show()
