# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *

class PerlPpixQuotelike(PerlPackage):
    """ 
 Parse Perl string literals and string-literal-like things.
"""
    homepage = "https://metacpan.org/pod/PPIx::QuoteLike"
    url = "https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-QuoteLike-0.023.tar.gz"
    version("0.023", sha256="3576a3149d2c53e07e9737b7892be5cfb84a499a6ef1df090b713b0544234d21",preferred=True)
    maintainers("rxy900") 
