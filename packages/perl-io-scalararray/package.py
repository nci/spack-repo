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
#     spack install perl-io-scalararray
#
# You can edit this file again by typing:
#
#     spack edit perl-io-scalararray
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------


from spack.package import *
class PerlIoScalararray(PerlPackage):
    """ IO:: interface for reading/writing an array of scalars
"""
    homepage = "https://metacpan.org/pod/IO::ScalarArray"
    url = "https://cpan.metacpan.org/authors/id/C/CA/CAPOEIRAB/IO-Stringy-2.113.tar.gz"
    version("2.113", sha256="51220fcaf9f66a639b69d251d7b0757bf4202f4f9debd45bdd341a6aca62fe4e",preferred=True)


