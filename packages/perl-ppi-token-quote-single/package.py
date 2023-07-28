# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
class PerlPpiTokenQuoteSingle(PerlPackage):
    """ 
A 'single quote' token
"""
    homepage = "https://metacpan.org/pod/PPI::Token::Quote::Single"
    url = "https://cpan.metacpan.org/authors/id/O/OA/OALDERS/PPI-1.276.tar.gz"
    version("1.276", sha256="657655470e78b7c5b7660f7dec82893489c2e2d880e449135613da3b37500f01",preferred=True)
    depends_on("perl-clone", type=("run"))
    maintainers("rxy900")
