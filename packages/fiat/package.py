# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install fiat
#
# You can edit this file again by typing:
#
#     spack edit fiat
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Fiat(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://github.com/ecmwf-ifs/fiat"
    url = "https://github.com/ecmwf-ifs/fiat/archive/refs/tags/1.1.0.zip"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    maintainers("rxy900")

    version("1.1.0", sha256="01b0b346fd6a4c28b8668511966e81959842ecfdb54289913165779ed9ac46c4")

    # FIXME: Add dependencies if required.
    depends_on("ecbuild")

    variant("mpi",default=False,description="Use MPI")
    depends_on("mpi",when="+mpi")

    variant("omp",default=False,description="Use OpenMP")

    def cmake_args(self):
        args = [
            self.define_from_variant("ENABLE_MPI","mpi"),
            self.define_from_variant("ENABLE_OMP","omp")
            ]
        return args


    def setup_build_environment(self, env):
        spec = self.spec
        env.set("CC", spec["mpi"].mpicc)
        env.set("CXX", spec["mpi"].mpicxx)
        env.set("FC", spec["mpi"].mpifc)
