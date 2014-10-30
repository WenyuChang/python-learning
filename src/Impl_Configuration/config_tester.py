__author__ = 'wenychan'


from configuration import MyConfiguration

config = MyConfiguration()
# config.show_all_properties()

print config

# print config.prop8
# print config.prop9
#
# print config.get()
# print config.get(section='section2')
print config.get(section='section2', option='prop8')