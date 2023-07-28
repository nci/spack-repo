# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlConfigTiny(PerlPackage):
    """
Read/Write .ini style files with as little code as possible
"""
    maintainers("rxy900")
    homepage = "https://metacpan.org/pod/Config::Tiny"
    url = "https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/Config-Tiny-2.29.tgz"
    version("2.29", sha256="3de79b0ea03a8d6a93e9d9128fe845fb556222b14699a4f6f0d5ca057ae3333b",preferred=True)


