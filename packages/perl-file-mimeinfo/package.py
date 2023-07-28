# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import inspect
class PerlFileMimeinfo(PerlPackage):
    """This module can be used to determine the mime type of a file. It tries to implement the freedesktop specification for a shared MIME database. For this module shared-mime-info-spec 0.13 was used. This package only uses the globs file. No real magic checking is used. The File::MimeInfo::Magic package is provided for magic typing. If you want to determine the mimetype of data in a memory buffer you should use File::MimeInfo::Magic in combination with IO::Scalar. This module loads the various data files when needed. If you want to hash data earlier see the rehash methods below.
"""
    homepage = "https://metacpan.org/pod/File::MimeInfo"
    url = "https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-MimeInfo-0.33.tar.gz"
    version("0.33", sha256="f6bea6b3890621325ec9c2792afaee88e948a0ae1d10872fa72c7110b3e1b1c4",preferred=True)
    maintainers("rxy900")
    depends_on("perl-file-basedir", type=("build", "run"))



