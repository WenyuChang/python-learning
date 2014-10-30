try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    

setup(
    ######################### Basic Information Section ######################################
    # metadata for project and will be uploaded to PyPI
    name='Setuptools Usage',
    version='1.0',
    author = "Wenyu",
    author_email = "xxx@cisco.com",
    maintiner = "Wenyu",
    maintiner_email = "wenychan@cisco.com",
    description = "This is Crypto Package",
    long_description="test test",
    download_url="http://www.cisco.com",
    license = "xxx",
    keywords = "crypto package",
    url = "http://www.cisco.com",   # project home page, if any

    ######################### Required Package&Script Section ######################################
    # packages = find_packages('src'),  # include all packages under src
    # package_dir = {'':'src'},   # packages are under src
    # find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]) # Exclusion package patterns
    packages=find_packages(), # find packages automatically by setuptools

    # if the first line of the script starts with #! and contains the word “python”, the Distutils
    # will adjust the first line to refer to the current interpreter location. By default, it is replaced
    # with the current interpreter location.
    scripts = ['say_hello.py'],

    ######################### Dependency Section ######################################
    # Project uses plumbum and M2Crypto, so ensure that the plumbum get
    # installed or upgraded on the target machine
    install_requires = ['plumbum>=1.4.0',
                        'M2Crypto==0.22.3'],

    # A list of strings naming URLs to be searched when satisfying dependencies. These links
    # will be used if needed to install packages specified by setup_requires or tests_require.
    # They will also be written into the egg's metadata for use by tools like EasyInstall to
    # use when installing an .egg file.
    # dependency_links = ['https://www.cisco.com',
    #                     'https://www.another.com'],


    ######################### Package Data Section ######################################
    # If set to True, this tells setuptools to automatically include any data files it finds
    # inside your package directories, that are either under CVS or Subversion control, or
    # which are specified by your MANIFEST.in file. Default is True
    # include_package_data = True
    
    # package_data = {
    #        # If any package contains *.txt or *.rst files, include them:
    #        '': ['*.txt', '*.doc'],
    #        # And include any *.type files found in the 'otherFiles' package, too:
    #        'otherFiles': ['*.type'],
    # },

    # ...but exclude README.txt from all packages
    # exclude_package_data = { '': ['README.txt'] },


    ######################### Others ######################################
    # A boolean (True or False) flag specifying whether the project can be safely
    # installed and run from a zip file. If this argument is not supplied, the bdist_egg
    # command will have to analyze all of your project's contents for possible problems each time it buids an egg.
    # One caveat is that you will have to always set zip_safe = False
    # in setup.py so that all the files are unzipped during installation.
    # zip_safe=True,
)