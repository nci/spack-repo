from spack.package import *

class FiatUm(CMakePackage):
    """Revised Fiat to make dr_hook working with UM."""

    homepage = "https://github.com/ecmwf-ifs/fiat"
    git = "https://github.com/MartinDix/fiat"
    version("1.1.0", branch="um")

    maintainers("rxy900")

    depends_on("ecbuild")
    depends_on("mpi")

    def cmake_args(self):
        args = ["-DCMAKE_BUILD_TYPE=Release","-DENABLE_MPI=ON","-DENABLE_OMP=ON"]
        return args




