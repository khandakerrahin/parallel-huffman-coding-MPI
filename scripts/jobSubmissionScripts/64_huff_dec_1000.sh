#!/bin/bash

#PBS -l select=1:ncpus=64:mem=2gb

# set max execution time
#PBS -l walltime=0:03:00
#PBS -q short_cpuQ
module load valgrind-3.15.0
module load mpich-3.2
#ls -lrt
#mpirun.actual -n 4 valgrind ./rahin_01/HuffmanEncoder rahin_01/input.txt
#mpirun --version

#encode
#mpirun.actual -n 4 valgrind --leak-check=full --show-leak-kinds=all ./shaker_huffman/parallel-huffman-codec/huffman -e /home/shaker.khandaker/inputFiles/100000000_words.txt /home/shaker.khandaker/encodedFiles/100000000_words_encoded.bin

# 64 cpu
mpirun.actual -n 64 valgrind --leak-check=full --show-leak-kinds=all ./shaker_huffman/bin/MPI_decompress /home/shaker.khandaker/encodedFiles/64_1000_words_encoded.bin /home/shaker.khandaker/decodedFiles/64_1000_words.txt