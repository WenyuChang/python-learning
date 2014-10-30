__author__ = 'wenychan'

from configuration import MyConfiguration

# # initialize configuration
# config = MyConfiguration()
# config = MyConfiguration('app')
# config = MyConfiguration('app', default_options={'option1':'value1'}, option2='value2', option3=333)

# # print out all the configurations
# config.show_all_properties()
# config.show_all_properties(raw=False) # raw means it will not replace %(xxx)s in the configuration

# # basic getting properties
# print config.prop1
# print config.prop2

# # advanced getting properties
# print config.get() # return a two-level dictionary contains all the sections and options
# print config.get(section='section') # return a one-level dictionary contains all the options in that section
# print config.get(option='option') # return this option's value if exists
# print config.get(section='section', option='option') # return specific option's value in specific section if exists
# print config.get(..., raw=True/False) # set if value is raw
# print config.get(..., option1='value1', option2=222222) # set values in parser

config = MyConfiguration()
#config = MyConfiguration(default_options={'aaa':'bbb'})
print config.aaa