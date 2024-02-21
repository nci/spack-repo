import os
from spack.package import *
class Um(Package):
    """UM is a numerical weather prediction and climate modelling software pacakge."""

    homepage = "https://code.metoffice.gov.uk/trac/um"
    # https://code.metoffice.gov.uk/trac/um/wiki/PastReleases
    version("13.4", revision=120750,svn="file:///g/data/ki32/mosrs/um/main/trunk/fcm-make")
    version("13.3", revision=118802,svn="file:///g/data/ki32/mosrs/um/main/trunk/fcm-make")
    version("13.2", revision=116723,svn="file:///g/data/ki32/mosrs/um/main/trunk/fcm-make")
    version("13.1", revision=114076,svn="file:///g/data/ki32/mosrs/um/main/trunk/fcm-make")
    version("13.0", revision=107106,svn="file:///g/data/ki32/mosrs/um/main/trunk/fcm-make")

    maintainers("rxy900")

    depends_on("fcm", type="build")
    depends_on("mpi", type=("build","run"))
    depends_on("eccodes+fortran", type=("build","link"))
    depends_on("netcdf-fortran", type=("build","link"))
    depends_on("gcom", type=("build","link"))
    depends_on("ecbuild", type=("build","link"))
    depends_on("fiat-um", type=("build","link"))


    variant("platform", default="intel", description="Build with MPI",
            values=("oneapi","intel"), multi=False)
    variant("omp",default=True,description="Use OpenMP")
    variant("netcdf",default=True,description="NetCDF")
    variant("opt",default="high",description="Optimization level",
            values=("high","safe","debug","rigorous"), multi=False)
    variant("eccodes",default=True,description="Using eccodes")
    variant("drhook",default=False,description="Using DRHOOK")
    variant("threadutils",default=False,description="using threadutils")

    def setup_build_environment(self, env):
        env.prepend_path("CPATH", self.spec["netcdf-fortran"].prefix.include)
        env.prepend_path("CPATH", self.spec["netcdf-c"].prefix.include)
        env.prepend_path("CPATH", self.spec["gcom"].prefix.include)
        env.prepend_path("CPATH", self.spec["eccodes"].prefix.include)
        env.prepend_path("LIBRARY_PATH", self.spec["netcdf-fortran"].prefix.lib)
        env.prepend_path("LIBRARY_PATH", self.spec["netcdf-c"].prefix.lib)
        env.prepend_path("LIBRARY_PATH", self.spec["gcom"].prefix.lib)
        env.prepend_path("LIBRARY_PATH", self.spec["eccodes"].prefix.lib64)


        env.prepend_path("CPATH", self.spec["fiat-um"].prefix.include)
        env.set("config_root_path","./")
        env.set("config_type","atmos")
        env.set("fcflags_overrides","")
        env.set("gwd_ussp_precision","double")
        env.set("land_surface_model","jules")
        env.set("ldflags_overrides_prefix","")
        env.set("ldflags_overrides_suffix","")
        env.set("ls_precipitation_precision","double")
        env.set("mirror","mirror")
        env.set("mpp_version","1C")
        env.set("platagnostic","false")
        env.set("portio_version","2A")
        env.set("stash_version","1A")
        env.set("timer_version","3A")

    def setup_run_environment(self, env):
        env.prepend_path("LD_LIBRARY_PATH", self.spec["netcdf-c"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["netcdf-fortran"].prefix.lib)
        env.prepend_path("LD_LIBRARY_PATH", self.spec["eccodes"].prefix.lib64)

    def install(self, spec, prefix):

        fcm=which("fcm")

        env["drhook"]="false"
        if "+drhook" in spec:
            env["DR_HOOK"]="true"

        env["platform_config_dir"]="nci-x86-ifort"
        platform = "nci-x86-ifort"
        if "platform=oneapi" in spec:
            env["platform_config_dir"]="nci-x86-ifx"
            platform="nci-x86-ifx"

        env["optimisation_level"]=spec.variants["opt"].value
        opt_value=spec.variants["opt"].value

        env["openmp"]="true"
        if "~omp" in spec:
            env["openmp"]="false"

        env["netcdf"]="true"
        if "~netcdf" in spec:
            env["netcdf"]="false"

        env["eccodes"]="true"
        if "~eccodes" in spec:
            env["eccodes"]="false"

        env["threadutils"]="false"
        if "+threadutils" in spec:
            env["thread_utils"]="true"


        # Build with fcm
        fcm("make", "-f", f"{platform}/um-atmos-{opt_value}.cfg", "--jobs=6")

        # Install
        mkdirp(prefix.bin)
        install("build-atmos/bin/um-atmos", prefix.bin + "/um-atmos")
        install("build-atmos/bin/um-atmos.exe", prefix.bin + "/um-atmos.exe")
        install("build-atmos/bin/um_script_functions", prefix.bin + "/um_script_functions")
        install("build-recon/bin/um-recon", prefix.bin + "/um-recon")
        install("build-recon/bin/um-recon.exe", prefix.bin + "/um-recon.exe")


        
