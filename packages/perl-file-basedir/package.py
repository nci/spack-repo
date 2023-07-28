# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
class PerlFileBasedir(PerlPackage):
    """ This module can be used to find directories and files as specified by the Freedesktop.org Base Directory Specification. This specifications gives a mechanism to locate directories for configuration, application data and cache data. It is suggested that desktop applications for e.g. the GNOME, KDE or Xfce platforms follow this layout. However, the same layout can just as well be used for non-GUI applications.
This module forked from File::MimeInfo.
This module follows version 0.6 of BaseDir specification.
"""
    maintainers("rxy900")
    homepage = "https://metacpan.org/pod/File::BaseDir"
    url = "https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/File-BaseDir-0.09.tar.gz"
    version("0.09", sha256="6da6f7281562ac8f11ef1a3af6aedb51c41182b60f1f122ced0079efd92967d9",preferred=True)



