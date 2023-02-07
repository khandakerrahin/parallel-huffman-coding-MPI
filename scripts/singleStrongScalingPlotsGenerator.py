import matplotlib.pyplot as plt

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]

# for file size 6.5MB
# without resource request
#times = [3.941, 2.082, 1.223, 0.861, 2.123, 1.971, 3.263, 4.476]
# with resource request
times = [3.941, 2.174, 1.0870, 1.135, 0.874, 1.317, 1.263, 1.476]
# Plot the results
plt.plot(num_procs, times, '-o', label='Result scaling')
plt.xscale('log', base=2)
plt.xlabel('Number of Processors')
plt.ylabel('Processing Time (s)')
plt.title('Strong Scaling: 6.5MB file')

# Plot the ideal case of linear scaling
plt.plot(num_procs, [times[0]/p for p in num_procs], '--', label='Ideal scaling')

# # Plot the ideal case of constant scaling
# plt.plot(num_procs, [times[0] for p in num_procs], '--', label='Constant Efficiency')

# Add a legend
plt.legend()

# Show the plot
plt.show()
