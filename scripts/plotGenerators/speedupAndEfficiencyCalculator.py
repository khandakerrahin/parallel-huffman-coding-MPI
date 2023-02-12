import pandas as pd

def calc_speedup(serial_time, parallel_time):
    return serial_time / parallel_time

def calc_efficiency(serial_time, parallel_time, num_procs):
    return serial_time / (parallel_time * num_procs)

num_procs = [1, 2, 4, 8, 16, 32, 64, 128]
problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]

# encoding 10 average times
serial_times = [0.1139, 0.12630000000000002, 15.620899999999997, 77.7251, 136.96959999999999, 282.0045, 404.0563]
parallel_times_02 = [0.27060000000000006, 0.32220000000000004, 12.575699999999998, 64.13950000000001, 127.6076, 246.5371, 380.0223]
parallel_times_04 = [0.40700000000000003, 0.8429, 8.4299, 47.185500000000005, 83.737, 161.772, 254.40220000000005]
parallel_times_08 = [1.0769, 0.9260999999999999, 6.871300000000001, 22.407100000000003, 41.8563, 79.4507, 114.2355]
parallel_times_16 = [1.2311, 1.1174, 3.9939, 12.3525, 23.6808, 43.53340000000001, 59.7182]
parallel_times_32 = [1.399, 1.5835000000000001, 3.1914, 8.922799999999999, 18.483299999999996, 34.521100000000004, 47.097100000000005]
parallel_times_64 = [1.5032000000000003, 1.4367, 2.9044, 9.840500000000002, 16.0848, 28.806, 44.4726]
parallel_times_128 = [6.297, 4.9166, 7.838199999999999, 12.3759, 19.2373, 30.811899999999998, 42.2904]

# decoding 10 average times
# serial_times = [0.0859, 0.1248, 15.774700000000001, 69.872, 119.0972, 274.23889999999994, 399.59729999999996]
# parallel_times_02 = [0.2627, 0.3225, 15.448599999999999, 66.40270000000001, 130.1733, 253.8784, 387.9851]
# parallel_times_04 = [0.2814, 0.3911, 10.967, 43.2666, 83.8355, 178.4211, 230.93200000000002]
# parallel_times_08 = [0.6478, 0.8113000000000001, 9.5623, 26.708800000000004, 45.2959, 85.2452, 118.77659999999999]
# parallel_times_16 = [1.0257999999999998, 1.2344, 6.2732, 14.6512, 27.9132, 51.26640000000001, 67.3256]
# parallel_times_32 = [1.399, 2.0435, 5.0891, 11.894499999999999, 24.2025, 40.5877, 59.69540000000001]
# parallel_times_64 = [1.5032000000000003, 1.4367, 6.5533, 12.1522, 16.577599999999997, 31.1427, 50.955799999999996]
# parallel_times_128 = [6.297, 4.9166, 7.838199999999999, 12.3759, 26.994, 38.79540000000001, 54.1682]

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
