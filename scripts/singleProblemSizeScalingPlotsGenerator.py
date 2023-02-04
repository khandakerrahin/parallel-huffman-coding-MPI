import matplotlib.pyplot as plt
import numpy as np



# Input data
num_procs = [10, 20, 40, 50, 100]
problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

serial_times = [0.130, 0.200, 26.120, 123.250, 244.780, 485.920, 727.430]
parallel_times_10 = [0.390, 0.570, 5.240, 15.360, 37.660, 58.320, 83.220]
parallel_times_20 = [1.120, 0.950, 4.470, 9.960, 17.270, 29.160, 42.300]
parallel_times_40 = [1.210, 1.200, 7.620, 10.020, 16.090, 26.420, 34.290]
parallel_times_50 = [1.080, 1.000, 2.760, 9.810, 13.380, 20.090, 40.100]
parallel_times_100 = [1.110, 2.530, 2.980, 5.500, 11.590, 17.040, 22.440]

strong_scaling_10 = [serial_times[i]/parallel_times_10[i] for i in range(len(serial_times))]
strong_scaling_20 = [serial_times[i]/parallel_times_20[i] for i in range(len(serial_times))]
strong_scaling_40 = [serial_times[i]/parallel_times_40[i] for i in range(len(serial_times))]
strong_scaling_50 = [serial_times[i]/parallel_times_50[i] for i in range(len(serial_times))]
strong_scaling_100 = [serial_times[i]/parallel_times_100[i] for i in range(len(serial_times))]

fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs = axs.ravel()
#Ideal Strong Scaling
ideal_strong_scaling = [serial_times[i]/50 for i in range(len(problem_size))]

axs[0].plot(problem_size, strong_scaling_10, '-o', label='Strong Scaling 10 Procs')
axs[0].set_title('Strong Scaling 10 Procs')
axs[0].set_xlabel('Problem Size')
axs[0].set_ylabel('Speedup')
axs[0].plot(problem_size, ideal_strong_scaling, '-o', color='red', label='Ideal Scaling')
axs[0].legend()

axs[1].plot(problem_size, strong_scaling_20, '-o', label='Strong Scaling 20 Procs')
axs[1].set_title('Strong Scaling 20 Procs')
axs[1].set_xlabel('Problem Size')
axs[1].set_ylabel('Speedup')
axs[1].plot(problem_size, ideal_strong_scaling, '-o', color='red', label='Ideal Scaling')
axs[1].legend()

axs[2].plot(problem_size, strong_scaling_40, '-o', label='Strong Scaling 40 Procs')
axs[2].set_title('Strong Scaling 40 Procs')
axs[2].set_xlabel('Problem Size')
axs[2].set_ylabel('Speedup')
axs[2].plot(problem_size, ideal_strong_scaling, '-o', color='red', label='Ideal Scaling')
axs[2].legend()

axs[3].plot(problem_size, strong_scaling_50, '-o', label='Strong Scaling 50 Procs')
axs[3].set_title('Strong Scaling 50 Procs')
axs[3].set_xlabel('Problem Size')
axs[3].set_ylabel('Speedup')
axs[3].plot(problem_size, ideal_strong_scaling, '-o', color='red', label='Ideal Scaling')

axs[3].legend()

axs[4].plot(problem_size, strong_scaling_100, '-o', label='Strong Scaling 100 Procs')
axs[4].set_title('Strong Scaling 100 Procs')
axs[4].set_xlabel('Problem Size')
axs[4].set_ylabel('Speedup')
axs[4].plot(problem_size, ideal_strong_scaling, '-o', color='red', label='Ideal Scaling')

axs[4].legend()

plt.tight_layout()
#plt.show()

# Calculate weak_scaling_time
parallel_times = [parallel_times_10, parallel_times_20, parallel_times_40, parallel_times_50, parallel_times_100]
weak_scaling_time = []
for i in range(len(parallel_times)):
    weak_scaling_time.append(parallel_times[i][0] * num_procs[i] / num_procs[0])

# Plot Weak Scaling
plt.figure()
plt.plot(num_procs, weak_scaling_time, '-o', label='Actual Scaling')
plt.xlabel('Number of Processors')
plt.ylabel('Execution Time (s)')

# Ideal Weak Scaling
ideal_weak_scaling = [num_procs[i] * serial_times[i] / num_procs[i] for i in range(len(num_procs))]
plt.plot(num_procs, ideal_weak_scaling, '-o', color='red', label='Ideal Scaling')


plt.title('Weak Scaling')
plt.legend()
plt.show()