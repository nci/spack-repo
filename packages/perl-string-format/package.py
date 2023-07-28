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
#     spack install perl-string-format
#
# You can edit this file again by typing:
#
#     spack edit perl-string-format
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlStringFormat(PerlPackage):
    """ 
sprintf-like string formatting capabilities with arbitrary format definitions
"""
    homepage = "https://metacpan.org/pod/String::Format"
    url = "https://cpan.metacpan.org/authors/id/S/SR/SREZIC/String-Format-1.18.tar.gz"
    version("1.18", sha256="9e417a8f8d9ea623beea2d13a47c0d5a696fc8602c0509b826cd45f97b76e778"
            ,preferred=True)


