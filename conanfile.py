from conans import ConanFile, CMake

class BoostShmemConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = "boost/1.78.0"
    generators = "cmake", "gcc", "txt"

