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
#     spack install perl-file-mimeinfo
#
# You can edit this file again by typing:
#
#     spack edit perl-file-mimeinfo
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
import inspect
class PerlFileMimeinfo(PerlPackage):
    """This module can be used to determine the mime type of a file. It tries to implement the freedesktop specification for a shared MIME database. For this module shared-mime-info-spec 0.13 was used. This package only uses the globs file. No real magic checking is used. The File::MimeInfo::Magic package is provided for magic typing. If you want to determine the mimetype of data in a memory buffer you should use File::MimeInfo::Magic in combination with IO::Scalar. This module loads the various data files when needed. If you want to hash data earlier see the rehash methods below.
"""

    homepage = "https://metacpan.org/pod/File::MimeInfo"
    url = "https://cpan.metacpan.org/authors/id/M/MI/MICHIELB/File-MimeInfo-0.33.tar.gz"
    version("0.33", sha256="f6bea6b3890621325ec9c2792afaee88e948a0ae1d10872fa72c7110b3e1b1c4",preferred=True)

    # According to cpandeps.grinnz.com Module-Build is both a build and run
    # time dependency for BioPerl
#    depends_on("perl-module-build", type=("build", "run"))
    depends_on("perl-file-basedir", type=("build", "run"))
#    depends_on("perl-io-scalararray", type=("build", "run"))
#    depends_on("perl-critic", type=("build", "run"))
#    depends_on("perl-readonly", type=("build", "run"))
#    depends_on("perl-exception-class",type=("build", "run"))
#    depends_on("perl-graph", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-http-message", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-io-stringy", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-ipc-run", type=("build", "run"))
#    depends_on("perl-list-moreutils", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-set-scalar", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-test-requiresinternet", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-dom", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-dom-xpath", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-libxml", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-sax", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-sax-base", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-sax-writer", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-twig", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-xml-writer", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-yaml", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-libwww-perl", when="@1.7.6:", type=("build", "run"))
#    depends_on("perl-libxml-perl", when="@1.7.6:", type=("build", "run"))



