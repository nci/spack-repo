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
#     spack install perl-config-tiny
#
# You can edit this file again by typing:
#
#     spack edit perl-config-tiny
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlConfigTiny(PerlPackage):
    """
Read/Write .ini style files with as little code as possible
"""
    homepage = "https://metacpan.org/pod/Config::Tiny"
    url = "https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-2.29.tgz"
    version("2.29", sha256="3de79b0ea03a8d6a93e9d9128fe845fb556222b14699a4f6f0d5ca057ae3333b",preferred=True)


