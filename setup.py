import sys
from setuptools import setup

if sys.version_info[0] == 2:
    if not sys.version_info >= (2, 7):
        raise ValueError('This package requires Python 2.7 or newer')
elif sys.version_info[0] == 3:
    if not sys.version_info >= (3, 3):
        raise ValueError('This package requires Python 3.3 or newer')
else:
    raise ValueError('Unrecognized major version of Python')

__project__ = 'shortcutter'
__desc__ = 'A cross platform simple api for setup.py and command line application for creating shortcuts (fork of Shortcut)'
__version__ = '0.0.2'
__author__ = "Martin O'Hanlon, Peter Zagubisalo"
__author_email__ = 'peter.zagubisalo@gmail.com'
__license__ = 'MIT'
__url__ = 'https://github.com/kiwi0fruit/shortcutter'
__install_requires__ = ['winshell;platform_system=="Windows"',
                        'pywin32;platform_system=="Windows"']


__classifiers__ = [
    "Development Status :: 3 - Alpha",
#    "Development Status :: 4 - Beta",
#    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: End Users/Desktop",
    "Topic :: Desktop Environment",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Environment :: MacOS X",
    "Environment :: Win32 (MS Windows)",
]

if __name__ == '__main__':
    setup(name='shortcutter',
          version = __version__,
          description = __desc__,
          url = __url__,
          author = __author__,
          author_email = __author_email__,
          license= __license__,
          packages = [__project__],
          install_requires = __install_requires__,
          entry_points={
              'console_scripts': [
                  'shortcutter = shortcutter:main'
                  ]},
          zip_safe=False)
