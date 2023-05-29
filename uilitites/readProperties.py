# how to read config.ini fie
import configparser

# creating object for configparser
config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")  # it is used for read config.ini file


class ReadConfig:

    @staticmethod
    def getAplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUserEmial():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password