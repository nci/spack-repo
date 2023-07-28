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
#     spack install perl-critic
#
# You can edit this file again by typing:
#
#     spack edit perl-critic
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlCritic(PerlPackage):
    """ 
Critique Perl source code for best-practices.
"""
    homepage = "https://metacpan.org/pod/Perl::Critic"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Perl-Critic-1.150.tar.gz"
    version("1.150",sha256="e5cd95de3e43bce70775176274baa405f326fc8740df0054bb816975cc8d349b",preferred=True)
    depends_on("perl-b-keywords", type=("build", "run"))
    depends_on("perl-list-someutils", type=("build", "run"))
    depends_on("perl-module-implementation", type=("build", "run"))
    depends_on("perl-readonly", type=("run"))
    depends_on("perl-exception-class", type=("run"))
    depends_on("perl-ppi-token-quote-single", type=("run"))
    depends_on("perl-module-pluggable", type=("run"))
    depends_on("perl-string-format", type=("run"))
    depends_on("perl-ppix-utils-traversal", type=("run"))
    depends_on("perl-pod-spell", type=("run"))
    depends_on("perl-tidy", type=("run"))
    depends_on("perl-ppix-quotelike", type=("run"))
    depends_on("perl-ppix-regexp", type=("run"))
    depends_on("perl-lingua-en-inflect", type=("run"))
    depends_on("perl-config-tiny", type=("run"))
    depends_on("perl-class-tiny", type=("run"))    
