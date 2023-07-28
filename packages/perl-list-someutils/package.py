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
#     spack install perl-list-someutils
#
# You can edit this file again by typing:
#
#     spack edit perl-list-someutils
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
class PerlListSomeutils(PerlPackage):
    """ 
Provide the stuff missing in List::Util
"""
    homepage = "https://metacpan.org/pod/List::SomeUtils"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/List-SomeUtils-0.59.tar.gz"
    version("0.59",sha256="fab30372e4c67bf5a46062da38d1d0c8756279feada866eb439fa29571a2dc7b",preferred=True)

