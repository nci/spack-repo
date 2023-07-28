# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PerlPodSpell(PerlPackage):
    """ 
a formatter for spellchecking Pod
"""
    homepage = "https://metacpan.org/pod/Pod::Spell"
    url = "https://cpan.metacpan.org/authors/id/H/HA/HAARG/Pod-Spell-1.26.tar.gz"
    version("1.26", sha256="2f05bfc9cfb04b96fcbfa2c8544d1e6ae908596d3696c46e0e26556b750afbbf",preferred=True)
    depends_on("perl-file-sharedir-install", type=("build", "run"))
    maintainers("rxy900")    

