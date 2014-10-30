__author__ = 'wenychan'


def print_traceback():
    # note! importing the traceback module messes up the
    # exception state, so you better do that here and not
    # in the exception handler
    import traceback
    try:
        raise SyntaxError, "example"
    except:
        traceback.print_exc()


def traceback_to_string():
    import traceback
    import StringIO
    try:
        raise IOError, "an i/o error occurred"
    except:
        fp = StringIO.StringIO()
        traceback.print_exc(file=fp)
        message = fp.getvalue()
    print "failure! the error was:", repr(message)


traceback_to_string()