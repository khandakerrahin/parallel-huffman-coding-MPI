import pandas as pd

def calc_speedup(serial_time, parallel_time):
    return serial_time / parallel_time

def calc_efficiency(serial_time, parallel_time, num_procs):
    return serial_time / (parallel_time * num_procs)

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]
problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

serial_times = [0.182, 0.247, 26.526, 120.928, 259.392, 510.843, 770.098]
parallel_times_02 = [0.587, 0.586, 15.652, 66.813, 135.695, 260.933, 393.236]
parallel_times_04 = [0.640, 0.565, 18.031, 44.436, 77.930, 148.644, 201.511]
parallel_times_08 = [1.028, 0.999, 11.890, 36.917, 49.655, 86.005, 147.186]
parallel_times_16 = [1.160, 1.202, 10.536, 29.439, 48.067, 72.573, 78.564]
parallel_times_32 = [1.949, 0.792, 14.895, 25.510, 34.972, 60.959, 72.995]
parallel_times_64 = [2.640, 4.852, 10.266, 17.791, 25.097, 57.127, 65.740]
parallel_times_128 = [36.723, 39.420, 39.432, 37.680, 53.439, 49.110, 67.820]

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

print("\n")

efficiencies_df = pd.DataFrame(efficiencies, columns=problem_size, index=num_procs)
print(efficiencies_df)
