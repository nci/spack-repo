# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PerlPpixUtilsTraversal(PerlPackage):
    """ 
Utility functions for traversing PPI documents
"""
    homepage = "https://metacpan.org/pod/PPIx::Utils::Traversal"
    url = "https://cpan.metacpan.org/authors/id/D/DB/DBOOK/PPIx-Utils-0.003.tar.gz"
    version("0.003", sha256="2a9bccfc8ead03be01b67248fe8e152522040f798286fa4ef4432b7f2efdba11",preferred=True)
    maintainers("rxy900")
