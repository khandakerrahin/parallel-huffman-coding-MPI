import os
import csv


problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]
serial_times = [0.2278, 0.25260000000000005, 27.3558, 136.2582, 273.93919999999997, 486.18500000000006, 697.7926]
parallel_times_02 = [0.2806, 0.33440000000000003, 12.980599999999999, 65.65079999999999, 133.2928, 258.0054, 391.38620000000003]
parallel_times_04 = [0.4596, 0.6601999999999999, 7.1568, 47.586400000000005, 86.40219999999998, 160.459, 250.35860000000002]
parallel_times_08 = [0.807, 0.8166, 6.9468000000000005, 20.8286, 40.0004, 77.7696, 119.3828]
parallel_times_16 = [0.3632, 0.4135999999999999, 3.0471999999999997, 9.717400000000001, 21.2834, 40.9566, 56.248599999999996]
parallel_times_32 = [1.1234, 1.4136, 3.1317999999999997, 8.505999999999998, 20.287, 35.36220000000001, 46.4054]
parallel_times_64 = [1.209, 1.2234, 2.5514, 7.5969999999999995, 13.0524, 28.117399999999996, 38.8052]
parallel_times_128 = [1.209, 1.2234, 2.5514, 7.5969999999999995, 13.0524, 28.117399999999996, 38.8052]

def average_csv_files(directory, csv_files):
    avg_time = 0
    for file in csv_files:
        with open(os.path.join(directory, file), 'r') as f:
            reader = csv.reader(f)
            next(reader)  # skip the header
            for row in reader:
                avg_time += float(row[1])
    avg_time /= len(csv_files)
    return avg_time


def create_averages(parent_dir, codeType):
    problem_size = [1000, 10000, 10000000, 50000000, 100000000, 200000000, 300000000]
    serial_times = []
    parallel_times_02 = []
    parallel_times_04 = []
    parallel_times_08 = []
    parallel_times_16 = []
    parallel_times_32 = []
    parallel_times_64 = []
    parallel_times_128 = []

    serial_dir = os.path.join(parent_dir, 'serial')
    parallel_dir = os.path.join(parent_dir, 'parallel')

    for size in problem_size:
        serial_coding_files  = os.path.join(serial_dir, codeType)
        serial_files = [f"run_00{i + 1}_{size}_words.csv" for i in range(5)]
        serial_times.append(average_csv_files(serial_coding_files, serial_files))

        parallel_dirs = [os.path.join(parallel_dir, f"{c}core/{codeType}") for c in
                                  ["02", "04", "08", "16", "32", "64", "128"]]
        parallel_times = [average_csv_files(d, [f"run_00{i + 1}_{size}_words.csv" for i in range(5)]) for d in
                          parallel_dirs]
        parallel_times_02.append(parallel_times[0])
        parallel_times_04.append(parallel_times[1])
        parallel_times_08.append(parallel_times[2])
        parallel_times_16.append(parallel_times[3])
        parallel_times_32.append(parallel_times[4])
        parallel_times_64.append(parallel_times[5])
        parallel_times_128.append(parallel_times[6])

    return problem_size, serial_times, parallel_times_02, parallel_times_04, parallel_times_08, parallel_times_16, parallel_times_32, parallel_times_64, parallel_times_128


if __name__ == '__main__':
    parent_dir = "C:/Users/shake/git/parallel-huffman-coding-MPI/outputs"
    problem_size, serial_times, parallel_times_02, parallel_times_04, parallel_times_08, parallel_times_16, parallel_times_32, parallel_times_64, parallel_times_128 = create_averages(
        parent_dir, 'encoding')
    print("problem_size =", problem_size)
    print("Encoding times: \n\n")
    print("problem_size =", problem_size)
    print("serial_times =", serial_times)
    print("parallel_times_02 =", parallel_times_02)
    print("parallel_times_04 =", parallel_times_04)
    print("parallel_times_08 =", parallel_times_08)
    print("parallel_times_16 =", parallel_times_16)
    print("parallel_times_32 =", parallel_times_32)
    print("parallel_times_64 =", parallel_times_64)
    print("parallel_times_128 =", parallel_times_128)

    print("Decoding times: \n\n")

    problem_size, serial_times, parallel_times_02, parallel_times_04, parallel_times_08, parallel_times_16, parallel_times_32, parallel_times_64, parallel_times_128 = create_averages(
        parent_dir, 'decoding')
    print("problem_size =", problem_size)
    print("serial_times =", serial_times)
    print("parallel_times_02 =", parallel_times_02)
    print("parallel_times_04 =", parallel_times_04)
    print("parallel_times_08 =", parallel_times_08)
    print("parallel_times_16 =", parallel_times_16)
    print("parallel_times_32 =", parallel_times_32)
    print("parallel_times_64 =", parallel_times_64)
    print("parallel_times_128 =", parallel_times_128)
