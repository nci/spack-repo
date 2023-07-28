# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PerlTidy(PerlPackage):
    """ 
Parses and beautifies perl source
"""
    homepage = "https://metacpan.org/dist/Perl-Tidy/view/lib/Perl/Tidy.pod"
    url = "https://cpan.metacpan.org/authors/id/S/SH/SHANCOCK/Perl-Tidy-20230701.tar.gz"
    version("20230701", sha256="e04922ba34a0c0c8dca7d6897a70399e1b1358441f66d3abd0f021a413869743",preferred=True)
    maintainers("rxy900")

