from conans import ConanFile, CMake
import os


class ZMQTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("*.dll", "bin", "bin")
        self.copy("*.dylib", "bin", "lib")

    def test(self):
        print ("Running test")
        os.chdir("bin")
        server = ".%sserver" % os.sep
        import subprocess
        pid = subprocess.Popen(server)
        print ("Lets launch client for ", server)
        self.run(".%sclient > null" % os.sep)
        pid.terminate()
