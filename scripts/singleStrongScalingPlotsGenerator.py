import matplotlib.pyplot as plt

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]
times = [25.816, 13.985, 12.952, 5.208, 6.871, 6.784, 7.347, 12.588]

# Plot the results
plt.plot(num_procs, times, '-o', label='Result scaling')
plt.xscale('log', base=2)
plt.xlabel('Number of Processors')
plt.ylabel('Execution Time (s)')
plt.title('Strong Scaling')

# Plot the ideal case of linear scaling
plt.plot(num_procs, [times[0]/p for p in num_procs], '--', label='Ideal scaling')

# # Plot the ideal case of constant scaling
# plt.plot(num_procs, [times[0] for p in num_procs], '--', label='Constant Efficiency')

# Add a legend
plt.legend()

# Show the plot
plt.show()
