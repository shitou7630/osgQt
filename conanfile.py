from conans import ConanFile, ConfigureEnvironment, CMake, RunEnvironment
from conans.tools import download
from conans.tools import unzip, replace_in_file
from conans import tools

import os
import string
from stat import *

class osgQtConan(ConanFile):
    name = "osgQt"
    version = "3.5.6"
    sources = "sources"
    generators = "cmake", "txt", "virtualenv"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False],
               "minosx": ['10.7', '10.8', '10.9', '10.10', '10.11']
               }

    default_options = "shared=True", "minosx=10.7"

    url="http://github.com/OpenSceneGraph/osgQt"
    license="LGPL"
    requires = "osg/3.5.6@cstb/stable" \
             , "Qt/5.9.0@cstb/stable"

    def config_options(self):
        if self.settings.os == "Macos":
            self.deps_cpp_info.cflags.append("-mmacosx-version-min=%s" % self.options.minosx)
            self.deps_cpp_info.cppflags.append("-mmacosx-version-min=%s" % self.options.minosx)
        else:
            self.options.remove('minosx')

        for lib in self.requires:
            lib_name = string.split(lib,'/')[0]
            self.options[lib_name].shared = self.options.shared
            if self.settings.os == "Macos":
                self.options[lib_name].minosx = self.options.minosx

    def package_id(self):
        if self.settings.os == 'Macos':
            self.info.settings.compiler.version = 'Any'

    def requirements(self):
        pass

    def imports(self):
        if self.scope.dev:
            if not self.scope.bundle:
                self.copy(pattern="qt.conf", dst="bin", src="bin")
                self.copy(pattern="*.dll", dst="bin", src="bin")
                self.copy(pattern="*.dylib", dst="bin", src="lib")
                self.copy(pattern="*.so*", dst="bin", src="lib")
                self.copy(pattern="*.dylib", dst="plugins", src="plugins")
                self.copy(pattern="*.dll", dst="plugins", src="plugins")
                self.copy(pattern="*.so*", dst="plugins", src="plugins")
                self.copy(pattern="*", dst="bin", src="libexec")
                self.copy(pattern="*", dst="data", src="data")
                self.copy(pattern="*", dst="data", src="share/gdal")
                self.copy(pattern="*", dst="data", src="Resources")
                self.copy(pattern="*.pdb", dst="bin", src="lib")
                self.copy(pattern="*.pdb", dst="bin", src="bin")
            self.copy(pattern="*", dst="translations", src="translations")
            self.copy(pattern="*.pak", dst="resources", src="resources")
            self.copy(pattern="*.dat", dst="resources", src="resources")
            self.copy(pattern="QtWebEngineProcess*", dst="bin", src="libexec")
            self.copy(pattern="QtWebEngineProcess*", dst="bin", src="bin")

    def source(self):
        pass

    def build(self):
        pass

    def package(self):
        # nothing to do here now
        pass

    def package_info(self):
        pass
