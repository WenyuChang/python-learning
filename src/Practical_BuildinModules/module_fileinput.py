__author__ = 'wenychan'


def output_text_file():
    # Example: Using the fileinput module to loop over a text file
    # File:fileinput-example-1.py
    import fileinput
    import sys
    for line in fileinput.input("samples/sample.txt"):
        sys.stdout.write("-> ")
        sys.stdout.write(line)

    # -> We will perhaps eventually be writing only small
    # -> modules which are identified by name as they are
    # -> used to build larger ones, so that devices like
    # -> indentation, rather than delimiters, might become
    # -> feasible for expressing local structure in the
    # -> source language.
    # -> -- Donald E. Knuth, December 1974


def output_multi_file():
    # Example: Using the fileinput module to process multiple files
    # File:fileinput-example-2.py
    import fileinput
    import glob
    import string
    import sys
    for line in fileinput.input(glob.glob("samples/*.txt")):
        if fileinput.isfirstline(): # first in a file?
            sys.stderr.write("-- reading %s --\n" % fileinput.filename())
            sys.stdout.write(str(fileinput.lineno()) + " " + string.upper(line))

    # -- reading samples\sample.txt --
    # 1 WE WILL PERHAPS EVENTUALLY BE WRITING ONLY SMALL
    # 2 MODULES WHICH ARE IDENTIFIED BY NAME AS THEY ARE
    # 3 USED TO BUILD LARGER ONES, SO THAT DEVICES LIKE
    # 4 INDENTATION, RATHER THAN DELIMITERS, MIGHT BECOME
    # 5 FEASIBLE FOR EXPRESSING LOCAL STRUCTURE IN THE
    # 6 SOURCE LANGUAGE.
    # 7 -- DONALD E. KNUTH, DECEMBER 1974