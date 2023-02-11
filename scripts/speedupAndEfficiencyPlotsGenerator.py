import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def calc_speedup(serial_time, parallel_time):
    return serial_time / parallel_time


def calc_efficiency(serial_time, parallel_time, num_procs):
    return serial_time / (parallel_time * num_procs)

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]

problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]


# encoding average times
# serial_times = [0.2278, 0.25260000000000005, 27.3558, 136.2582, 273.93919999999997, 486.18500000000006, 697.7926]
# parallel_times_02 = [0.2806, 0.33440000000000003, 12.980599999999999, 65.65079999999999, 133.2928, 258.0054, 391.38620000000003]
# parallel_times_04 = [0.4596, 0.6601999999999999, 7.1568, 47.586400000000005, 86.40219999999998, 160.459, 250.35860000000002]
# parallel_times_08 = [0.807, 0.8166, 6.9468000000000005, 20.8286, 40.0004, 77.7696, 119.3828]
# parallel_times_16 = [0.3632, 0.4135999999999999, 3.0471999999999997, 9.717400000000001, 21.2834, 40.9566, 56.248599999999996]
# parallel_times_32 = [1.1234, 1.4136, 3.1317999999999997, 8.505999999999998, 20.287, 35.36220000000001, 46.4054]
# parallel_times_64 = [1.209, 1.2234, 2.5514, 7.5969999999999995, 13.0524, 28.117399999999996, 38.8052]
# parallel_times_128 = [4.226, 4.228199999999999, 7.2042, 9.6866, 15.884000000000004, 27.5388, 38.9066]

# decoding average times
serial_times = [0.1718, 0.2496, 28.0394, 122.48800000000001, 238.1944, 477.7398, 690.5226]
parallel_times_02 = [0.2386, 0.3032, 14.837799999999998, 68.7988, 135.957, 268.7324, 398.5524]
parallel_times_04 = [0.2819999999999999, 0.40800000000000003, 9.649600000000001, 43.8352, 78.56199999999998, 171.0154, 236.661]
parallel_times_08 = [0.789, 0.8316000000000001, 9.4804, 22.798, 43.254799999999996, 80.95179999999999, 112.56120000000001]
parallel_times_16 = [0.37559999999999993, 0.384, 5.813000000000001, 12.708000000000002, 29.1928, 51.629200000000004, 64.8588]
parallel_times_32 = [1.1234, 1.9466, 5.3048, 11.996, 24.2416, 40.6084, 61.9]
parallel_times_64 = [1.209, 1.2234, 5.912999999999999, 10.2058, 15.534199999999998, 28.032999999999998, 49.0724]
parallel_times_128 = [4.226, 4.228199999999999, 7.2042, 9.6866, 20.740199999999998, 28.630599999999998, 44.057399999999994]

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
    plt.xscale('log', base=2)
    plt.xlabel("Number of processors")
    plt.ylabel("Speedup")
    plt.title("Speedup vs Number of processors")
    plt.legend(title="Word count")

plt.subplot(1, 2, 2)
for column in efficiencies_df.columns:
    plt.plot(efficiencies_df.index, efficiencies_df[column], label=str(column))
    plt.xscale('log', base=2)
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
plt.title('Huffman Decoding: Performance Comparison of Different cores')
plt.legend()
plt.show()