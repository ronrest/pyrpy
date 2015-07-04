"""A setuptools based setup module.
See:
setup.py code based on code from here:
https://github.com/pypa/sampleproject/blob/master/setup.py
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
#-------------------------------------------------------------------------------
#                                                        Extract info from files
#-------------------------------------------------------------------------------
# Extract version number from VERSION file
version_file = path.join(path.dirname(__file__), 'pyrpy', 'VERSION')
with open(version_file, encoding='utf-8') as f:
    version = f.read().strip()

# Extract long description from DESCRIPTION.rst file
with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

#-------------------------------------------------------------------------------
#                                                                          Setup
#-------------------------------------------------------------------------------
setup(
    name='pyrpy',
    version=version,
    license='MIT',
    keywords = ['R', 'statistics', 'data analysis'],

    description='R-Style functions for Python',
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/ronrest/pyrpy',

    # Author details
    maintainer = "Ronny Restrepo",
    maintainer_email = "ronny.coding@gmail.com",
    author = "Ronny Restrepo",
    author_email = "ronny.coding@gmail.com",

    # Classifiers.
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers = [
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',

        'Operating System :: OS Independent',

        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Information Analysis',
        ],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),

    # DEPENDENCIES
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html

    #install_requires=['somePackage'],

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]

    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.

    #package_data={
    #    'sample': ['package_data.dat'],
    #},

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'

    #data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
