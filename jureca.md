The system has 2 sockets of 12-core Haswell on each node.

Slurm doen't play nicely with hyperthreading, so stick to one thread per core:

```
cumming1@jrl12:affinity > srun -n1 -c12 ./test.mpi
affinity test for 1 MPI ranks
rank      0 @ jrc0613
  thread   0 on cores [0:11]
  thread   1 on cores [0:11]
  thread   2 on cores [0:11]
  thread   3 on cores [0:11]
  thread   4 on cores [0:11]
  thread   5 on cores [0:11]
  thread   6 on cores [0:11]
  thread   7 on cores [0:11]
  thread   8 on cores [0:11]
  thread   9 on cores [0:11]
  thread  10 on cores [0:11]
  thread  11 on cores [0:11]

cumming1@jrl12:affinity > srun -n2 -c12 ./test.mpi
affinity test for 2 MPI ranks
rank      0 @ jrc0613
  thread   0 on cores [0:11]
  thread   1 on cores [0:11]
  thread   2 on cores [0:11]
  thread   3 on cores [0:11]
  thread   4 on cores [0:11]
  thread   5 on cores [0:11]
  thread   6 on cores [0:11]
  thread   7 on cores [0:11]
  thread   8 on cores [0:11]
  thread   9 on cores [0:11]
  thread  10 on cores [0:11]
  thread  11 on cores [0:11]
rank      1 @ jrc0613
  thread   0 on cores [12:23]
  thread   1 on cores [12:23]
  thread   2 on cores [12:23]
  thread   3 on cores [12:23]
  thread   4 on cores [12:23]
  thread   5 on cores [12:23]
  thread   6 on cores [12:23]
  thread   7 on cores [12:23]
  thread   8 on cores [12:23]
  thread   9 on cores [12:23]
  thread  10 on cores [12:23]
  thread  11 on cores [12:23]
```
