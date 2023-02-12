import os
import csv


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
    problem_size = [1000]

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
        #serial_files = [f"run_00{i + 1}_{size}_words.csv" for i in range(5)]
        serial_files = [f"run_00{i + 1}_6.5MB_text.csv" for i in range(10)]
        serial_times.append(average_csv_files(serial_coding_files, serial_files))

        parallel_dirs = [os.path.join(parallel_dir, f"{c}core/{codeType}") for c in
                                  ["02", "04", "08", "16", "32", "64", "128"]]
        parallel_times = [average_csv_files(d, [f"run_00{i + 1}_6.5MB_text.csv" for i in range(10)]) for d in
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

    print("\n\nDecoding times: \n\n")

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
