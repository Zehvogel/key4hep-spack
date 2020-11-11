from spack import *
from spack.pkg.k4.Ilcsoftpackage import k4_add_latest_commit_as_version

class K4fwcore(CMakePackage):
    """Core framework components of the Key4HEP project"""
    homepage = "https://github.com/key4hep/k4FWCore"
    url = "https://github.com/key4hep/k4FWCore/archive/v00-01.tar.gz"
    git = "https://github.com/key4hep/k4FWCore.git"

    version('master', branch='master')
    k4_add_latest_commit_as_version(git)
    version('0.2.0', sha256='7d1a6e7494f08c2b25901cab2138795f21b6c4e84f05c4f8b9a6839787874b72')
    version('0.1.1', sha256='9c4e4b487f7d9c982547c13570345399505e763fb369b76ceadb35c1d52bf6aa')
    version('0.1.0', sha256='aef682649f3fcb1d72de897fbf6ec4ed421c8a4836bb3462c4b0049a709374e4')


    variant('build_type', default='Release',
            description='CMake build type',
            values=('Debug', 'Release', 'RelWithDebInfo', 'MinSizeRel'))

    variant('cxxstd',
            default='17',
            values=('14', '17'),
            multi=False,
            description='Use the specified C++ standard when building.')

    depends_on('gaudi@32.2:')
    depends_on('root@6.08:')
    depends_on('podio@0.10:')

    def cmake_args(self):
        args = []
        # C++ Standard
        args.append('-DCMAKE_CXX_STANDARD=%s' % self.spec.variants['cxxstd'].value)
        # Setting this bypasses the get_binary_tag.py script
        # and a check for BINARY_TAG which is not used in this build system
        # should become obsolete with the cmake modernisation in gaudi v34
        if self.spec.satisfies('^gaudi@:34.99'):
          args.append('-DHOST_BINARY_TAG=x86_64-linux-gcc9-opt')
        return args

    def url_for_version(self, version):
        # releases are dashes and padded with a leading zero
        # the patch version is omitted when 0
        # so for example v01-12-01, v01-12 ...
        major = (str(version[0]).zfill(2))
        minor = (str(version[1]).zfill(2))
        patch = (str(version[2]).zfill(2))
        if version[2] == 0:
            url = "https://github.com/key4hep/k4FWCore/archive/v%s-%s.tar.gz" % (major, minor)
        else:
            url = "https://github.com/key4hep/k4FWCore/archive/v%s-%s-%s.tar.gz" % (major, minor, patch)
        return url
    
    def setup_run_environment(self, spack_env):
        spack_env.prepend_path('PYTHONPATH', self.prefix.python)
        spack_env.prepend_path("PATH", self.prefix.scripts)
	