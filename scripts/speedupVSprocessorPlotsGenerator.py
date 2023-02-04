def calc_speedup(serial_time, parallel_time):
    return serial_time / parallel_time

def calc_efficiency(parallel_time, num_procs):
    return calc_speedup(serial_times[0], parallel_time) / num_procs

num_procs = [10, 20, 40, 50, 100]
problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

serial_times = [0.130, 0.200, 26.120, 123.250, 244.780, 485.920, 727.430]
parallel_times_10 = [0.390, 0.570, 5.240, 15.360, 37.660, 58.320, 83.220]
parallel_times_20 = [1.120, 0.950, 4.470, 9.960, 17.270, 29.160, 42.300]
parallel_times_40 = [1.210, 1.200, 7.620, 10.020, 16.090, 26.420, 34.290]
parallel_times_50 = [1.080, 1.000, 2.760, 9.810, 13.380, 20.090, 40.100]
parallel_times_100 = [1.110, 2.530, 2.980, 5.500, 11.590, 17.040, 22.440]

parallel_times = [parallel_times_10, parallel_times_20, parallel_times_40, parallel_times_50, parallel_times_100]

speedups = []
efficiencies = []
for i, p_times in enumerate(parallel_times):
    speedup = [calc_speedup(serial_times[j], p_times[j]) for j in range(len(serial_times))]
    efficiency = [calc_efficiency(p_times[j], num_procs[i]) for j in range(len(serial_times))]
    speedups.append(speedup)
    efficiencies.append(efficiency)

print("Speedups:")
for i, num_proc in enumerate(num_procs):
    print(f"Num Procs: {num_proc}")
    for j, prob_size in enumerate(problem_size):
        print(f"Problem Size: {prob_size} Speedup: {speedups[i][j]}")
    print("\n")

print("Efficiencies:")
for i, num_proc in enumerate(num_procs):
    print(f"Num Procs: {num_proc}")
    for j, prob_size in enumerate(problem_size):
        print(f"Problem Size: {prob_size} Efficiency: {efficiencies[i][j]}")
    print("\n")
