__author__ = 'wenychan'

from setuptools import setup, find_packages # this is new

setup(name='packaging-test',
    version='1.0',
    packages=find_packages(),

    install_requires = ['plumbum>=1.4.0'],

    # The data files must be under CVS or Subversion control,
    # or else they must be specified via the distutils' MANIFEST.in file
    # include_package_data = True

    package_data = {
            # If any package contains *.txt or *.rst files, include them:
            '': ['*.txt', '*.doc'],
            # And include any *.msg files found in the 'hello' package, too:
            'otherFiles': ['*.type'],
    },

    # ...but exclude README.txt from all packages
    exclude_package_data = { '': ['README.txt'] },

    # One caveat is that you will have to also set zip_safe = False
    # in setup.py so that all the files are unzipped during installation.
    zip_safe=True,

    # metadata for upload to PyPI
    author = "Wenyu",
    author_email = "xxx@cisco.com",
    description = "This is Crypto Package",
    license = "xxx",
    keywords = "crypto package",
    url = "http://www.cisco.com",   # project home page, if any
)