import os
import configparser


def get_file_path(filename):
    directory = os.path.dirname(__file__)
    return os.path.join(directory, filename)

def get_file_content(filename):
    # Utils directory, i.e. webapp directory
    filepath =  get_file_path(filename)   
    file = open(filepath, 'r')
    return file.read()

def get_configurations(filename):
    filepath = get_file_path(filename)
    config = configparser.ConfigParser()
    config.read(filepath)
    return config
