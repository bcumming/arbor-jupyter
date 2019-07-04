### environment ###

# set up environment for building on the multicore part of jureca
module purge
module use /usr/local/software/jureca/OtherStages/
module load Stages/2019a

module load GCC
module load ParaStationMPI
module load CMake

module load Python/3.6.8
module load SciPy-Stack/2019a-Python-3.6.8 
module load Jupyter

module load mpi4py/3.0.1-Python-3.6.8

export base_path=$(pwd)
export repo_path=$(pwd)/repo
export build_path=$(pwd)/build
export install_path=$(pwd)/install

export arb_mpi=on
export arb_gpu=off
export arb_arch=native

export CC=`which mpicc`
export CXX=`which mpicxx`
export PYTHONPATH="${install_path}/lib/python3.6/site-packages":$PYTHONPATH

