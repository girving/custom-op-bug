import os
from distutils.core import Extension, setup
import pkg_resources
import sys
from tensorflow.python.platform import sysconfig

os.environ['CC'] = 'g++'
mac = sys.platform == 'darwin'
debug = False
custom = Extension(
    name='custom',
    sources=['custom.cc'],
    language='c++',
    extra_compile_args=['-std=c++1z', '-Wall', '-Werror', '-Wno-sign-compare'] +
                       ['-g', '-UNDEBUG'] * debug +
                       ['-Wthread-safety', '-stdlib=libc++'] * mac +
                       sysconfig.get_compile_flags(),
    extra_link_args=sysconfig.get_link_flags() + ['-undefined', 'dynamic_lookup'] * mac,
)

setup(name='safety',
    version='0.0.1',
    py_modules=['safety'],
    ext_modules=[custom],
)
