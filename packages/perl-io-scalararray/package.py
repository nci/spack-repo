# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
class PerlIoScalararray(PerlPackage):
    """ IO:: interface for reading/writing an array of scalars
"""
    homepage = "https://metacpan.org/pod/IO::ScalarArray"
    url = "https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/IO-Stringy-2.113.tar.gz"
    version("2.113", sha256="51220fcaf9f66a639b69d251d7b0757bf4202f4f9debd45bdd341a6aca62fe4e",preferred=True)
    maintainers("rxy900")

