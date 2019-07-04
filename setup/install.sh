git clone https://github.com/arbor-sim/arbor.git --recursive "$repo_path"

mkdir "$build_path"
cd "$build_path"
cmake "$repo_path"                 \
    -DARB_WITH_PYTHON=on           \
    -DARB_ARCH=$arb_arch           \
    -DARB_WITH_MPI=$arb_mpi        \
    -DARB_WITH_GPU=$arb_gpu        \
    -DCMAKE_C_COMPILER="$CC"       \
    -DCMAKE_CXX_COMPILER="$CXX"    \
    -DCMAKE_INSTALL_PREFIX=${install_path}
make -j8
make install
cd "$base_path"
