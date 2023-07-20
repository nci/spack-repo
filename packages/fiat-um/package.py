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

    def setup_build_environment(self, env):
        spec = self.spec
        env.set("CC", spec["mpi"].mpicc)
        env.set("CXX", spec["mpi"].mpicxx)
        env.set("FC", spec["mpi"].mpifc)

    def setup_run_environment(self, env):
        env.prepend_path("CPATH", self.prefix.include.fiat)
        env.prepend_path("CPATH", self.prefix.module.fiat)
        env.prepend_path("CPATH", self.prefix.module.parkind_dp)
        env.prepend_path("FPATH", self.prefix.include.fiat)
        env.prepend_path("FPATH", self.prefix.module.fiat)
        env.prepend_path("FPATH", self.prefix.module.parkind_dp)
