from configparser import ConfigParser
import logging

def read_configurations(category,key):
    config = ConfigParser()
    config.read("configurations/config.ini")
    return config.get(category,key)
