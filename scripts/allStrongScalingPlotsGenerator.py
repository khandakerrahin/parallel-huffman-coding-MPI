import matplotlib.pyplot as plt

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]
times = [25.816, 13.985, 12.952, 5.208, 6.871, 6.784, 7.347, 12.588]

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]
problem_sizes = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

# encoding time
# serial_times = [0.169, 0.205, 25.816, 122.013, 242.423, 505.358, 793.051]
# parallel_times_02 = [0.228, 0.669, 13.985, 70.625, 142.407, 265.116, 391.978]
# parallel_times_04 = [0.602, 0.479, 12.952, 39.043, 74.908, 141.161, 204.284]
# parallel_times_08 = [1.234, 1.559, 5.208, 17.930, 66.223, 112.695, 116.508]
# parallel_times_16 = [1.453, 3.792, 6.871, 26.834, 43.467, 69.234, 65.462]
# parallel_times_32 = [1.949, 6.637, 6.784, 25.077, 46.756, 80.859, 95.969]
# parallel_times_64 = [2.640, 4.852, 7.347, 12.595, 26.784, 35.200, 54.389]
# parallel_times_128 = [12.334, 10.681, 12.588, 15.704, 26.541, 38.275, 55.148]

# decoding time
serial_times = [0.182, 0.247, 26.526, 120.928, 259.392, 510.843, 770.098]
parallel_times_02 = [0.587, 0.586, 15.652, 66.813, 135.695, 260.933, 393.236]
parallel_times_04 = [0.640, 0.565, 18.031, 44.436, 77.930, 148.644, 201.511]
parallel_times_08 = [1.028, 0.999, 11.890, 36.917, 49.655, 86.005, 147.186]
parallel_times_16 = [1.160, 1.202, 10.536, 29.439, 48.067, 72.573, 78.564]
parallel_times_32 = [1.949, 0.792, 14.895, 25.510, 34.972, 60.959, 72.995]
parallel_times_64 = [2.640, 4.852, 10.266, 17.791, 25.097, 57.127, 65.740]
parallel_times_128 = [12.334, 10.681, 12.588, 15.704, 26.541, 38.275, 55.148]

parallel_times = [serial_times, parallel_times_02, parallel_times_04, parallel_times_08, parallel_times_16, parallel_times_32, parallel_times_64, parallel_times_128]

# # Plot the results for each problem size
# for i, problem_size in enumerate(problem_sizes):
#     times = [serial_times[i], parallel_times_02[i], parallel_times_04[i], parallel_times_08[i], parallel_times_16[i], parallel_times_32[i], parallel_times_64[i], parallel_times_128[i]]
#     # Plot the results
#     plt.plot(num_procs, times, '-o', label='Result scaling')
#     plt.xscale('log', base=2)
#     plt.xlabel('Number of Processors')
#     plt.ylabel('Processing Time (s)')
#     plt.title(f'Strong Scaling: {problem_size} words')
#
#     # Plot the ideal case of linear scaling
#     plt.plot(num_procs, [times[0] / p for p in num_procs], '--', label='Ideal scaling')
#
#     # # Plot the ideal case of constant scaling
#     # plt.plot(num_procs, [times[0] for p in num_procs], '--', label='Constant Efficiency')
#
#     # Add a legend
#     plt.legend()
#
#     # Show the plot
#     plt.show()

# Create a figure and subplots for each problem size
fig, axs = plt.subplots(nrows=4, ncols=2, figsize=(10, 10), sharex=True)

# Plot the results for each problem size
for i, (problem_size, ax) in enumerate(zip(problem_sizes, axs.flatten())):
    times = [serial_times[i], parallel_times_02[i], parallel_times_04[i], parallel_times_08[i], parallel_times_16[i], parallel_times_32[i], parallel_times_64[i], parallel_times_128[i]]
    # Plot the results
    ax.plot(num_procs, times, '-o', label='Result scaling')
    ax.set_xscale('log', base=2)
    ax.set_xlabel('Number of Processors')
    ax.set_ylabel('Processing Time (s)')
    ax.set_title(f'Decoding Strong Scaling: {problem_size} words')

    # Plot the ideal case of linear scaling
    ax.plot(num_procs, [times[0] / p for p in num_procs], '--', label='Ideal scaling')

    # # Plot the ideal case of constant scaling
    # plt.plot(num_procs, [times[0] for p in num_procs], '--', label='Constant Efficiency')

    # Add a legend
    ax.legend()

# Show the plot
plt.tight_layout()
plt.show()