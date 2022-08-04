import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class Readconfig():
    @staticmethod
    def getapplicationurl():
        url=config.get('common info', 'baseurl')
        return url

    @staticmethod
    def getusername():
        username=config.get('common info', 'username')
        return username

    @staticmethod
    def getpassword():
        password=config.get('common info', 'password')
        return password
    @staticmethod
    def getitemname():
        itemname=config.get('common info', 'itemname')
        return itemname

    @staticmethod
    def getfname():
        fname = config.get('common info', 'fname')
        return fname

    @staticmethod
    def getlname():
        lname = config.get('common info', 'lname')
        return lname

    @staticmethod
    def getpcode():
        pcode = config.get('common info', 'pcode')
        return pcode