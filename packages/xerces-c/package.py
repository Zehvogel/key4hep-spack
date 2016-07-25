from spack import *

class XercesC(Package):
    """ Xerces-C++ is a validating XML parser written in a portable subset of C++.
    Xerces-C++ makes it easy to give your application the ability to read and
    write XML data. A shared library is provided for parsing, generating,
    manipulating, and validating XML documents using the DOM, SAX, and SAX2 APIs.
    """

    homepage = "https://xerces.apache.org/xerces-c"
    url      = "https://www.apache.org/dist/xerces/c/3/sources/xerces-c-3.1.2.tar.gz"
    version('3.1.2', '9eb1048939e88d6a7232c67569b23985')
    version('3.1.3', '70320ab0e3269e47d978a6ca0c0e1e2d')
      
    def install(self, spec, prefix):
        configure("--prefix=%s" % prefix,
                  "--disable-network")
        make("clean")
        make()
        make("install")

