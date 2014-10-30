__author__ = 'wenychan'

from ConfigParser import SafeConfigParser

def usage():
    parser = SafeConfigParser()
    parser.read('my.config')

    for section_name in parser.sections():
        print 'Section:', section_name
        print '  Options:', parser.options(section_name)
        for name, value in parser.items(section_name):
            print '  %s = %s' % (name, value)
        print

def usage1():
    parser = SafeConfigParser()
    parser.read('my.config')
    print parser.get('section_one', 'url')
    print parser.get('section_one', 'username')
    print parser.get('section_one', 'password')
    print parser.get('section_one', 'flag')

def usage2():
    # The read() method also accepts a list of filenames.
    # Each name in turn is scanned, and if the file exists
    # it is opened and read.
    parser = SafeConfigParser()
    candidates = ['does_not_exist.ini', 'also-does-not-exist.ini',
                  'simple.ini', 'multisection.ini', 'my.config'
                  ]
    found = parser.read(candidates)
    print parser.get('section_one', 'url')
    print parser.get('section_one', 'username')
    print parser.get('section_one', 'password')
    missing = set(candidates) - set(found)

    print 'Found config files:', sorted(found)
    print 'Missing files     :', sorted(missing)

def usage3():
    # has section or option
    parser = SafeConfigParser()
    parser.read('my.config')

    for section in ['wiki', 'bug_tracker', 'dvcs', 'section_one']:
        print '%-12s: %s' % (section, parser.has_section(section))
        if parser.has_section(section):
            for candidate in [ 'username', 'password', 'url', 'description' ]:
                print '%s.%-12s  : %s' % (section, candidate, parser.has_option(section, candidate))
            print

def usage4():
    # Require values
    try:
        parser = SafeConfigParser()
        parser.read('allow_no_value.ini')
    except Exception as err:
        print 'Could not parse:', err

    # Allow stand-alone option names
    print '\nTrying again with allow_no_value=True'
    parser = SafeConfigParser(allow_no_value=True)
    parser.read('allow_no_value.ini')
    for flag in [ 'turn_feature_on', 'turn_other_feature_on' ]:
        print
        print flag
        exists = parser.has_option('flags', flag)
        print '  has_option:', exists
        if exists:
            print '         get:', parser.get('flags', flag)


def usage5():
    # Modifying Settings
    parser = SafeConfigParser()
    parser.read('my.config')
    parser.add_section('section_two')
    parser.set('section_two', 'url', 'http://localhost:8080/bugs')
    parser.set('section_two', 'username', 'dhellmann')
    parser.set('section_two', 'password', 'secret')

    for section in parser.sections():
        print section
        for name, value in parser.items(section):
            print '  %s = %r' % (name, value)

    parser.write(open('my.config', 'w'))

def usage6():
    # Option Search Path
    # If the option name appears in the vars dictionary passed to get(), the value from vars is returned.
    # If the option name appears in the specified section, the value from that section is returned.
    # If the option name appears in the DEFAULT section, that value is returned.
    # If the option name appears in the defaults dictionary passed to the constructor, that value is returned.

    # Define the names of the options
    option_names = [
        'from-default',
        'from-section', 'section-only',
        'file-only', 'init-only', 'init-and-file',
        'from-vars',
        ]

    # Initialize the parser with some defaults
    parser = SafeConfigParser(
        defaults={'from-default':'value from defaults passed to init',
                  'init-only':'value from defaults passed to init',
                  'init-and-file':'value from defaults passed to init',
                  'from-section':'value from defaults passed to init',
                  'from-vars':'value from defaults passed to init',
                  })

    print 'Defaults before loading file:'
    defaults = parser.defaults()
    for name in option_names:
        if name in defaults:
            print '  %-15s = %r' % (name, defaults[name])

    # Load the configuration file
    parser.read('searchpath.config')

    print '\nDefaults after loading file:'
    defaults = parser.defaults()
    for name in option_names:
        if name in defaults:
            print '  %-15s = %r' % (name, defaults[name])

    # Define some local overrides
    vars = {'from-vars':'value from vars'}

    # Show the values of all of the options
    print '\nOption lookup:'
    for name in option_names:
        value = parser.get('sect', name, vars=vars)
        print '  %-15s = %r' % (name, value)

    # Show error messages for options that do not exist
    print '\nError cases:'
    try:
        print 'No such option :', parser.get('sect', 'no-option')
    except Exception as err:
        print str(err)

    try:
        print 'No such section:', parser.get('no-sect', 'no-option')
    except Exception as err:
        print str(err)

def usage7():
    # Combining Values with Interpolation
    parser = SafeConfigParser()
    parser.read('interpolation.config.ini')

    print 'Original value       :', parser.get('bug_tracker', 'url')

    parser.set('bug_tracker', 'port', '9090')
    print 'Altered port value   :', parser.get('bug_tracker', 'url')

    print 'Without interpolation:', parser.get('bug_tracker', 'url', raw=True)

if __name__ == '__main__':
    # usage1()

    # usage2()

    # usage()

    # usage3()

    # usage4()

    # usage5()

    usage6()

    # usage7()