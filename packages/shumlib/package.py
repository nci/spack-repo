# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Shumlib(MakefilePackage):
    """Shumlib: collective of a set of libraries which are used by the UM."""
    homepage = "https://code.metoffice.gov.uk/trac/utils/wiki/shumlib"
    svn = "file:///g/data/ki32/mosrs/utils/shumlib/trunk"

    maintainers = ["rxy900"]

    version("um13.1", revision=6514)
    version("um13.2", revision=6731)
    version("um13.3", revision=6823)
    version("2022.11.1", revision=6514)
    version("2023.03.1", revision=6731)
    version("2023.06.1", revision=6823)    
    variant("platform", values=(["nci-x86","bom-xc40"]), default="nci-x86", description="", multi=False)
    patch("c_shum_compiler_select.patch" , when="@2023.06.1")
    
    def get_arch_comp(self):
        if self.spec.satisfies("%intel"):
            mach_c = "ifort-icc"
        elif self.spec.satisfies("%gcc"):
            mach_c = "gfortran-gcc"
        else:
            raise NotImplentedError("Unknown compiler")
        
        mach_m=self.spec.variants["platform"].value
        return mach_m+"-"+mach_c
    
    @property
    def makefile(self):
        makefile_name="make/"+self.get_arch_comp()+".mk"
        return makefile_name

    @property
    def source_directory(self):
        source_dir = self.stage.source_path
        return source_dir

    @property
    def build_directory(self):
        build_dir = self.get_arch_comp()
        return join_path("build",build_dir)
    
    
    def build(self,spec,prefix):        
        with spack.util.environment.set_env(PWD=self.source_directory):
            make("-j1","-f", self.makefile)
            make("fruit","-j1","-f", self.makefile)

    @run_after("build")
    def test(self):
        with spack.util.environment.set_env(PWD=self.source_directory):        
            make("test","-j1","-f", self.makefile)
        
    def install(self, spec, prefix):
        build_dir=self.build_directory
        install_tree(build_dir+"/lib", prefix.lib)
        install_tree(build_dir+"/include", prefix.include)
        install_tree(build_dir+"/tests", prefix.tests)
        
