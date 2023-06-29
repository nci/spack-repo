from spack.package import *

class Mom6(Package):
    """FIXME: Put a proper description of your package here."""

    homepage = ""
    git = "https://github.com/NOAA-GFDL/MOM6-examples.git"
    version("main",submodules=True)
    maintainers("rxy900")

    resource(
        name="mom6-ninja-nci",
        git="https://github.com/angus-g/mom6-ninja-nci.git",
        branch="master",
        destination="build",
    )

    depends_on("mpi", type=("build","run"))
    depends_on("netcdf-fortran", type=("build","link"))

    def install(self, spec, prefix):
        filter_file("srcdir=","srcdir="+self.stage.source_path+"/src",self.stage.source_path+"/build/mom6-ninja-nci/gen_build.sh")
        ninja=Executable("ninja")
        with working_dir(self.stage.source_path+"/build/mom6-ninja-nci"):
            gencmd=Executable(self.stage.source_path+"/build/mom6-ninja-nci/gen_build.sh")
            gencmd()

        with working_dir(self.stage.source_path+"/build/mom6-ninja-nci/shared"):
            gencmd=Executable(self.stage.source_path+"/build/mom6-ninja-nci/shared/gen_build.sh")
            gencmd()
            ninja()

        with working_dir(self.stage.source_path+"/build/mom6-ninja-nci/ice_ocean_SIS2_symmetric"):
            gencmd=Executable(self.stage.source_path+"/build/mom6-ninja-nci/ice_ocean_SIS2_symmetric/gen_build.sh")
            gencmd()
            ninja()

        mkdirp(prefix.bin)
        install("build/mom6-ninja-nci/ice_ocean_SIS2_symmetric/MOM6", prefix.bin + "/MOM6")
