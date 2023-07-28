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
#     spack install perl-b-keywords
#
# You can edit this file again by typing:
#
#     spack edit perl-b-keywords
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlBKeywords(PerlPackage):
    """ 
Lists of reserved barewords and symbol names
"""
    homepage = "https://metacpan.org/pod/B::Keywords"
    url = "https://cpan.metacpan.org/authors/id/R/RU/RURBAN/B-Keywords-1.26.tar.gz"
    version("1.26", sha256="2daa155d2f267fb0dedd87f8a4c4fb5663879fc106517b1ee258353ef87aed34",preferred=True)

