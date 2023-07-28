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
#     spack install perl-ppix-quotelike
#
# You can edit this file again by typing:
#
#     spack edit perl-ppix-quotelike
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlPpixQuotelike(PerlPackage):
    """ 
 Parse Perl string literals and string-literal-like things.
"""
    homepage = "https://metacpan.org/pod/PPIx::QuoteLike"
    url = "https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-QuoteLike-0.023.tar.gz"
    version("0.023", sha256="3576a3149d2c53e07e9737b7892be5cfb84a499a6ef1df090b713b0544234d21",preferred=True)
