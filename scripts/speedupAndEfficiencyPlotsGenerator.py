import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def calc_speedup(serial_time, parallel_time):
    return serial_time / parallel_time


def calc_efficiency(serial_time, parallel_time, num_procs):
    return serial_time / (parallel_time * num_procs)

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]
problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

# encoding time
serial_times = [0.169, 0.205, 25.816, 122.013, 242.423, 505.358, 793.051]
parallel_times_02 = [0.228, 0.669, 13.985, 70.625, 142.407, 265.116, 391.978]
parallel_times_04 = [0.602, 0.479, 12.952, 39.043, 74.908, 141.161, 204.284]
parallel_times_08 = [1.234, 1.559, 5.208, 17.930, 66.223, 112.695, 116.508]
parallel_times_16 = [1.453, 3.792, 6.871, 26.834, 43.467, 69.234, 65.462]
parallel_times_32 = [1.949, 6.637, 6.784, 25.077, 46.756, 80.859, 95.969]
parallel_times_64 = [2.640, 4.852, 7.347, 12.595, 26.784, 35.200, 54.389]
parallel_times_128 = [12.334, 10.681, 12.588, 15.704, 26.541, 38.275, 55.148]

# # decoding time
# serial_times = [0.182, 0.247, 26.526, 120.928, 259.392, 510.843, 770.098]
# parallel_times_02 = [0.587, 0.586, 15.652, 66.813, 135.695, 260.933, 393.236]
# parallel_times_04 = [0.640, 0.565, 18.031, 44.436, 77.930, 148.644, 201.511]
# parallel_times_08 = [1.028, 0.999, 11.890, 36.917, 49.655, 86.005, 147.186]
# parallel_times_16 = [1.160, 1.202, 10.536, 29.439, 48.067, 72.573, 78.564]
# parallel_times_32 = [1.949, 0.792, 14.895, 25.510, 34.972, 60.959, 72.995]
# parallel_times_64 = [2.640, 4.852, 10.266, 17.791, 25.097, 57.127, 65.740]
# parallel_times_128 = [12.334, 10.681, 12.588, 15.704, 26.541, 38.275, 55.148]

parallel_times = [serial_times, parallel_times_02, parallel_times_04, parallel_times_08, parallel_times_16, parallel_times_32, parallel_times_64, parallel_times_128]

speedups = []
efficiencies = []
for i, p_times in enumerate(parallel_times):
    speedup = [calc_speedup(serial_times[j], p_times[j]) for j in range(len(serial_times))]
    efficiency = [calc_efficiency(serial_times[j], p_times[j], num_procs[i]) for j in range(len(serial_times))]
    speedups.append(speedup)
    efficiencies.append(efficiency)

speedups_df = pd.DataFrame(speedups, columns=problem_size, index=num_procs)
print(speedups_df)
speedups_df.to_csv('speedups_df.csv')
print("\n")

efficiencies_df = pd.DataFrame(efficiencies, columns=problem_size, index=num_procs)
print(efficiencies_df)
efficiencies_df.to_csv('efficiencies_df.csv')

plt.figure(figsize=[10, 5])
plt.subplot(1, 2, 1)
for column in speedups_df.columns:
    plt.plot(speedups_df.index, speedups_df[column], label=str(column))
    plt.xlabel("Number of processors")
    plt.ylabel("Speedup")
    plt.title("Speedup vs Number of processors")
    plt.legend(title="Word count")

plt.subplot(1, 2, 2)
for column in efficiencies_df.columns:
    plt.plot(efficiencies_df.index, efficiencies_df[column], label=str(column))
    plt.xlabel("Number of processors")
    plt.ylabel("Efficiency")
    plt.title("Efficiency vs Number of processors")
    plt.legend(title="Word count")

plt.show()

problem_size = problem_size / np.max(problem_size)
plt.plot(serial_times, problem_size, label='Serial')
plt.plot(parallel_times_02, problem_size, label='Parallel with 2 Procs')
plt.plot(parallel_times_04, problem_size, label='4 Procs')
plt.plot(parallel_times_08, problem_size, label='8 Procs')
plt.plot(parallel_times_16, problem_size, label='16 Procs')
plt.plot(parallel_times_32, problem_size, label='32 Procs')
plt.plot(parallel_times_64, problem_size, label='64 Procs')
plt.plot(parallel_times_128, problem_size, label='128 Procs')

plt.xlabel('Time (s)')
plt.ylabel('Problem Size')
plt.title('Huffman Encoding: Performance Comparison of Different cores')
plt.legend()
plt.show()

# Plotting the data
plt.plot(num_procs, serial_times, label='Serial')
plt.plot(num_procs, parallel_times_02, label='Parallel, 2 processes')
plt.plot(num_procs, parallel_times_04, label='Parallel, 4 processes')
plt.plot(num_procs, parallel_times_08, label='Parallel, 8 processes')
plt.plot(num_procs, parallel_times_16, label='Parallel, 16 processes')
plt.plot(num_procs, parallel_times_32, label='Parallel, 32 processes')
plt.plot(num_procs, parallel_times_64, label='Parallel, 64 processes')
plt.plot(num_procs, parallel_times_128, label='Parallel, 128 processes')

# Adding labels and legend
plt.xlabel('Number of Processes')
plt.ylabel('Processing Time (s)')
plt.legend()

# Show the plot
plt.show()