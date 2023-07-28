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
#     spack install perl-lingua-en-inflect
#
# You can edit this file again by typing:
#
#     spack edit perl-lingua-en-inflect
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlLinguaEnInflect(PerlPackage):
    """
 Convert singular to plural. Select "a" or "an".
"""
    homepage = "https://metacpan.org/pod/Lingua::EN::Inflect"
    url = "https://cpan.metacpan.org/authors/id/D/DC/DCONWAY/Lingua-EN-Inflect-1.905.tar.gz"
    version("1.905", sha256="05c29ec3482e572313a60da2181b0b30c5db7cf01f8ae7616ad67e1b66263296",preferred=True)


