import configparser

config_file = configparser.RawConfigParser()
config_file.read("/path/to/config.conf")

config_file.has_option('section', 'option')