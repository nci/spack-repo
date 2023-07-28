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
#     spack install perl-ppi-token-quote-single
#
# You can edit this file again by typing:
#
#     spack edit perl-ppi-token-quote-single
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlPpiTokenQuoteSingle(PerlPackage):
    """ 

"""
    homepage = "https://metacpan.org/pod/PPI::Token::Quote::Single"
    url = "https://cpan.metacpan.org/authors/id/O/OA/OALDERS/PPI-1.276.tar.gz"
    version("1.276", sha256="657655470e78b7c5b7660f7dec82893489c2e2d880e449135613da3b37500f01",preferred=True)
    depends_on("perl-clone", type=("run"))
