__author__ = 'wenychan'

from ConfigParser import SafeConfigParser


class _FinalMeta(type):
    class ConstError(TypeError): pass
    def __setattr__(cls, name, value):
        if name in cls.__dict__ and name.isupper():
            raise cls.ConstError, "Can't rebind const(%s)" % name
        else:
            super(_FinalMeta, cls).__setattr__(name, value)


class MyConfiguration():
    __metaclass__ = _FinalMeta
    #__CONFIG_PATH = '/opt/cisco/etc'
    __CONFIG_PATH = '.'
    __DEFAULT_CONFIG_FILE = 'cesium.properties'

    def __init__(self, app='', service='', default_options=None, **kwargs):
        # default_options is used to set default value if it does not exist in the configuration files
        # kwargs or vars is used to reset values no matter if it exists in the configuration files
        # Option Search Path
            # If the option name appears in the vars dictionary passed to get(), the value from vars is returned.
            # If the option name appears in the specified section, the value from that section is returned.
            # If the option name appears in the DEFAULT section, that value is returned.
            # If the option name appears in the defaults dictionary passed to the constructor, that value is returned.

        self.__app = app.strip()
        self.__service = service.strip()
        self.__default_options = default_options
        self.__config_vars = {}
        for key, value in kwargs.items():
            self.__config_vars[key.upper()] = str(value)

        default_cfg_file = '{0}/{1}'.format(MyConfiguration.__CONFIG_PATH, MyConfiguration.__DEFAULT_CONFIG_FILE)
        config_candidate = [default_cfg_file]
        if len(self.__app) > 0:
            app_cfg_file = '{0}/{1}.{2}'.format(MyConfiguration.__CONFIG_PATH, self.__app, MyConfiguration.__DEFAULT_CONFIG_FILE)
            config_candidate.append(app_cfg_file)

        self.__parser = SafeConfigParser(defaults=self.__default_options, allow_no_value=True)
        found = self.__parser.read(config_candidate)
        if len(found) < 2 and len(self.__app) != 0:
            # TODO: log - configuration file not found
            print 'log - configuration file not found'
            pass

    def show_all_properties(self, raw=False):
        if self.__parser is None:
            # TODO: log - configuration is not initialized
            print 'log - configuration is not initialized'
            pass

        for section_name in self.__parser.sections():
            print 'Section: {0} ({1})'.format(section_name, [prop.upper() for prop in self.__parser.options(section_name)])
            for prop in self.__parser.options(section_name):
                value = self.__parser.get(section_name, prop, raw=raw, vars=self.__config_vars)
                value = self.__value_parse(prop.upper(), value)
                print '   {0} = {1}' .format(prop.upper(), value)

    def __value_parse(self, prop, value):
        value = True if value is None and prop.endswith('ON') else value
        if type(value) is str:
            value = value.strip()
            if value.isdigit():
                return int(value)
            else:
                try:
                    return float(value)
                except ValueError:
                    pass
        return value

    def __getattr__(self, args):
        args = args.upper()
        for section_name in self.__parser.sections():
            if self.__parser.has_option(section_name, args):
                value = self.__parser.get(section_name, args, raw=False, vars=self.__config_vars)
                return self.__value_parse(args, value)

        if args in self.__config_vars.keys():
            value = self.__config_vars[args]
            return self.__value_parse(args, value)

        # TODO: log - no such configuration property
        print 'log - no such configuration property'
        return None

    def get(self, section=None, option=None, raw=False, **kwargs):
        if len(kwargs) > 0 and option is not None:
            from copy import deepcopy
            tmp_parser = deepcopy(self.__parser)
            if section is not None:
                for key, value in kwargs.items():
                    if tmp_parser.has_option(section, key):
                        tmp_parser.set(section, key, value)
            else:
                for section_name in self.__parser.sections():
                    for key, value in kwargs.items():
                        if tmp_parser.has_option(section_name, key):
                            tmp_parser.set(section_name, key, value)
        else:
            tmp_parser = self.__parser

        if section is None and option is None:
            return self.__all_options(tmp_parser, raw)
        elif section is not None and option is None:
            return self.__options_against_section(tmp_parser, section, raw)
        elif section is None and option is not None:
            return self.__option_against_name(tmp_parser, option, raw)
        elif section is not None and option is not None:
            from ConfigParser import NoOptionError
            try:
                value = tmp_parser.get(section, option, raw=raw, vars=self.__config_vars)
            except NoOptionError:
                # TODO: log - no such configuration property
                print 'log - no such configuration property'
                return None
            else:
                return self.__value_parse(option.upper(), value)


    def __all_options(self, parser, raw=False):
        option_dict = {}
        for section_name in parser.sections():
            option_dict[section_name] = {}
            for prop in parser.options(section_name):
                value = parser.get(section_name, prop, raw=raw, vars=self.__config_vars)
                value = self.__value_parse(prop.upper(), value)
                option_dict[section_name][prop.upper()] = value
        return option_dict

    def __options_against_section(self, parser, section, raw):
        if parser.has_section(section):
            option_dict = {}
            for prop in parser.options(section):
                value = parser.get(section, prop, raw=raw, vars=self.__config_vars)
                value = self.__value_parse(prop.upper(), value)
                option_dict[prop.upper()] = value
            return option_dict
        else:
            # TODO log - no such section
            print 'log - no such section'
            return None

    def __option_against_name(self, parser, option, raw):
        option = option.upper()
        for section_name in self.__parser.sections():
            if self.__parser.has_option(section_name, option):
                value = self.__parser.get(section_name, option, raw=False, vars=self.__config_vars)
                return self.__value_parse(option, value)

        if option in self.__config_vars.keys():
            value = self.__config_vars[option]
            return self.__value_parse(option.upper(), value)

        # TODO: log - no such configuration property
        print 'log - no such configuration property'
        return None





