# <center> **Parallel Huffman Encoding and Decoding** </center>
**High Performance Computing for Data Science Project 2023 - UniTN**

The project aims to implement a Parallel Huffman Encoding and Decoding using MPI and perform benchmarks. 
We have evaluated the performance of our parallel Huffman coding implementation on several
randomly created text datasets of different sizes, and compared the results with those of existing
sequential and parallel implementations. Our results show that our implementation provides
substantial speedup compared to the sequential version, and is competitive with other parallel
implementations in terms of runtime. Additionally, we have also analyzed the scalability of our
implementation, and observed that it scales well with an increasing number of cores, thus
demonstrating its suitability for high-performance computing systems.

**Serial implementation:** [Click here](https://github.com/khandakerrahin/parallel-huffman-coding-MPI/tree/main/HuffmanCoder/Serial)

**MPI implementation:** [Click here](https://github.com/khandakerrahin/parallel-huffman-coding-MPI/tree/main/HuffmanCoder/MPI)

**Full report:** [Click here](https://github.com/khandakerrahin/parallel-huffman-coding-MPI/blob/main/report/parallel_huffman_coding_report.pdf)

## Serial
### How to compile & run

```bash
cd <dir of serial>
make
# to encode
bin/compress data/input.txt data/input.encoded.bin
# to decode
bin/decompress data/input.encoded.bin data/input.decoded.txt
# MPI run command 
mpiexec -n 1 ./shaker_huffman/bin/compress /home/shaker.khandaker/inputFiles/1000_words.txt /home/shaker.khandaker/encodedFiles/01_1000_words_encoded.bin
```

## Parallel
### How to compile & run
```bash
# load modules
module load valgrind-3.15.0
module load mpich-3.2
cd <dir of parallel>
make
# to encode
bin/MPI_compress data/input.txt data/input.encoded.bin
# to decode
bin/MPI_decompress data/input.encoded.bin data/input.decoded.txt
# MPI run command with valgrind
mpirun.actual -n 2 valgrind --leak-check=full --show-leak-kinds=all ./shaker_huffman/bin/MPI_decompress /home/shaker.khandaker/encodedFiles/02_10000_words_encoded.bin /home/shaker.khandaker/decodedFiles/02_10000_words.txt
```

### Submittting a job at the cluster
```bash
qsub -o /home/shaker.khandaker/results/outputs/parallel/128core/encoding/run_0011_6.5MB_text.csv 128_huff_enc_custom.sh
```
