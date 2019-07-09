### environment ###

# set up environment for building on the multicore part of jureca
export base_path=$(pwd)
export repo_path=$(pwd)/repo
export build_path=$(pwd)/build
export install_path=$(pwd)/install

export arb_mpi=on
export arb_gpu=off
export arb_arch=native

export CC=`which mpicc`
export CXX=`which mpicxx`
export PYTHONPATH="${install_path}/lib/python3.7/site-packages":$PYTHONPATH

