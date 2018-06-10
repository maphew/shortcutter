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


setup(
    name='shortcutter',
    version = '0.0.2',
    description = 'A cross platform simple api for setup.py and command line application for creating shortcuts (fork of Shortcut)',
    url = 'https://github.com/kiwi0fruit/shortcutter',
    author = "Martin O'Hanlon, Peter Zagubisalo",
    author_email = 'peter.zagubisalo@gmail.com',
    license= 'MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
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
    ],
    packages = ['shortcutter'],
    install_requires = ['pywin32;platform_system=="Windows"'],
    entry_points={
        'console_scripts': [
            'shortcutter = shortcutter:main'
        ]},
    zip_safe=False
)
