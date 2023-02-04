import matplotlib.pyplot as plt

# Add data here
serial_times = [0.130, 0.200, 26.120, 123.250, 244.780, 485.920, 727.430]
parallel_times_10 = [0.390, 0.570, 5.240, 15.360, 37.660, 58.320, 83.220]
parallel_times_20 = [1.120, 0.950, 4.470, 9.960, 17.270, 29.160, 42.300]
parallel_times_40 = [1.210, 1.200, 7.620, 10.020, 16.090, 26.420, 34.290]
parallel_times_50 = [1.080, 1.000, 2.760, 9.810, 13.380, 20.090, 40.100]
parallel_times_100 = [1.110, 2.530, 2.980, 5.500, 11.590, 17.040, 22.440]

# Calculate the speedup, efficiency, and scalability
speedup_10 = [serial_times[i]/parallel_times_10[i] for i in range(7)]
speedup_20 = [serial_times[i]/parallel_times_20[i] for i in range(7)]
speedup_40 = [serial_times[i]/parallel_times_40[i] for i in range(7)]
speedup_50 = [serial_times[i]/parallel_times_50[i] for i in range(7)]
speedup_100 = [serial_times[i]/parallel_times_100[i] for i in range(7)]

efficiency_10 = [speedup_10[i]/10 for i in range(7)]
efficiency_20 = [speedup_20[i]/20 for i in range(7)]
efficiency_40 = [speedup_40[i]/40 for i in range(7)]
efficiency_50 = [speedup_50[i]/50 for i in range(7)]
efficiency_100 = [speedup_100[i]/100 for i in range(7)]

# Plot the results
plt.figure()
plt.plot(serial_times, speedup_10, label='10 processors')
plt.plot(serial_times, speedup_20, label='20 processors')
plt.plot(serial_times, speedup_40, label='40 processors')
plt.plot(serial_times, speedup_50, label='50 processors')
plt.plot(serial_times, speedup_100, label='100 processors')
plt.xlabel('Serial Time (s)')
plt.ylabel('Speedup')
plt.legend()
plt.title('Speedup Plot')

plt.figure()
plt.plot(serial_times, efficiency_10, label='10 processors')
plt.plot(serial_times, efficiency_20, label='20 processors')
plt.plot(serial_times, efficiency_40, label='40 processors')
plt.plot(serial_times, efficiency_50, label='50 processors')
plt.plot(serial_times, efficiency_100, label='100 processors')
plt.xlabel('Serial Time (s)')
plt.ylabel('Efficiency')
plt.legend()
plt.title('Efficiency Plot')

plt.show()