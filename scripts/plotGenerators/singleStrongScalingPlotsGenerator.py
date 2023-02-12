import matplotlib.pyplot as plt

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]

# for file size 6.5MB
# without resource request
#times = [3.941, 2.082, 1.223, 0.861, 2.123, 1.971, 3.263, 4.476]
# with resource request
times = [4.211, 2.1894, 1.3464, 1.2804, 2.8222, 1.8386, 2.6782, 4.4836]
# with resource request and 10 average
times = [2.2848999999999995, 2.2351, 1.5485000000000002, 1.8893, 2.4956, 3.7978999999999994, 2.3634999999999997, 5.2963000000000005]
times = [4.211, 2.2351, 1.5485000000000002, 1.8893, 2.4956, 3.7978999999999994, 2.3634999999999997, 5.2963000000000005]


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