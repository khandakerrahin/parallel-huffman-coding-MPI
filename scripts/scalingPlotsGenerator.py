import matplotlib.pyplot as plt
import numpy as np



# Input data
num_procs = [10, 20, 40, 50, 100]
problem_size = [100, 200, 400, 500, 1000]
serial_times = [100, 200, 300, 400, 500, 600, 700]
parallel_times_10 = [10, 14, 17, 20, 50, 70, 85]
parallel_times_20 = [7, 11, 12, 15, 17, 22, 35]
parallel_times_40 = [5.25, 8.5, 9.75, 11, 12.22, 17.5, 18.95]
parallel_times_50 = [3, 6, 7.6, 8.24, 9.5, 10.6, 13.7]
parallel_times_100 = [0.85, 1.7, 1.99, 2.7, 2.99, 3.82, 5.5]

# Calculate strong_scaling_time
strong_scaling_time = []
parallel_times = [parallel_times_10, parallel_times_20, parallel_times_40, parallel_times_50, parallel_times_100]
for i in range(len(parallel_times)):
    strong_scaling_time.append(serial_times[0]/parallel_times[i][0])

# Plot Strong Scaling
plt.figure()
plt.plot(num_procs, strong_scaling_time, '-o', label='Actual Scaling')
plt.xlabel('Number of Processors')
plt.ylabel('Execution Time (s)')

# Ideal Strong Scaling
ideal_strong_scaling = strong_scaling_time[0]/np.array(num_procs)
plt.plot(num_procs, ideal_strong_scaling, '-o', color='red', label='Ideal Scaling')

plt.title('Strong Scaling')
plt.legend()
#plt.show()

# Calculate weak_scaling_time
weak_scaling_time = []
for i in range(len(parallel_times)):
    weak_scaling_time.append(parallel_times[i][0] * num_procs[i] / num_procs[0])

# Plot Weak Scaling
plt.figure()
plt.plot(num_procs, weak_scaling_time, '-o', label='Actual Scaling')
plt.xlabel('Number of Processors')
plt.ylabel('Execution Time (s)')

# Ideal Weak Scaling
ideal_weak_scaling = [num_procs[0] * serial_times[0] / num_procs[i] for i in range(len(num_procs))]
plt.plot(num_procs, ideal_weak_scaling, '-o', color='red', label='Ideal Scaling')


plt.title('Weak Scaling')
plt.legend()
plt.show()
