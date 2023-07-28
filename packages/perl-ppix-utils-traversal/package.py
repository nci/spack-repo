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
#     spack install perl-ppix-utils-traversal
#
# You can edit this file again by typing:
#
#     spack edit perl-ppix-utils-traversal
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlPpixUtilsTraversal(PerlPackage):
    """ 
Utility functions for traversing PPI documents
"""
    homepage = "https://metacpan.org/pod/PPIx::Utils::Traversal"
    url = "https://cpan.metacpan.org/authors/id/D/DB/DBOOK/PPIx-Utils-0.003.tar.gz"
    version("0.003", sha256="2a9bccfc8ead03be01b67248fe8e152522040f798286fa4ef4432b7f2efdba11",preferred=True)
