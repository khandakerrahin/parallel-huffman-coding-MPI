import matplotlib.pyplot as plt
import pandas as pd

def calc_speedup(serial_time, parallel_time):
    return serial_time / parallel_time


def calc_efficiency(serial_time, parallel_time, num_procs):
    return serial_time / (parallel_time * num_procs)

num_procs = [1, 10, 20, 40, 50, 100]
problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

# with clock()
serial_times = [0.130, 0.200, 26.120, 123.250, 244.780, 485.920, 727.430]
parallel_times_10 = [0.390, 0.570, 5.240, 15.360, 37.660, 58.320, 83.220]
parallel_times_20 = [1.120, 0.950, 4.470, 9.960, 17.270, 29.160, 42.300]
parallel_times_40 = [1.210, 1.200, 7.620, 10.020, 16.090, 26.420, 34.290]
parallel_times_50 = [1.080, 1.000, 2.760, 9.810, 13.380, 20.090, 40.100]
parallel_times_100 = [1.110, 2.530, 2.980, 5.500, 11.590, 17.040, 22.440]

# with MPI_WTime()
# serial_times = [0.0001, 0.0001, 28.000, 131.000, 261.000, 506.000, 751.000]
# parallel_times_10 = [1.000, 0.0001, 7.000, 17.000, 35.000, 63.000, 108.000]
# parallel_times_20 = [1.000, 2.000, 15.000, 27.000, 40.000, 71.000, 95.000]
# parallel_times_40 = [2.000, 4.000, 8.000, 20.000, 29.000, 41.000, 59.000]
# parallel_times_50 = [5.000, 3.000, 9.000, 16.000, 25.000, 47.000, 66.000]
# parallel_times_100 = [0.0001, 0.0001, 28.000, 131.000, 41.0000, 62.000, 75.000]

parallel_times = [serial_times, parallel_times_10, parallel_times_20, parallel_times_40, parallel_times_50, parallel_times_100]

speedups = []
efficiencies = []
for i, p_times in enumerate(parallel_times):
    speedup = [calc_speedup(serial_times[j], p_times[j]) for j in range(len(serial_times))]
    efficiency = [calc_efficiency(serial_times[j], p_times[j], num_procs[i]) for j in range(len(serial_times))]
    speedups.append(speedup)
    efficiencies.append(efficiency)

speedups_df = pd.DataFrame(speedups, columns=problem_size, index=num_procs)
print(speedups_df)

print("\n")

efficiencies_df = pd.DataFrame(efficiencies, columns=problem_size, index=num_procs)
print(efficiencies_df)

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
