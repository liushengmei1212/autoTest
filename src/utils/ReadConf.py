import configparser
import os

class ReadConf:
    root_dir = os.path.dirname(os.path.abspath('.'))
    cf = configparser.ConfigParser()
    cf.read(root_dir + "/config.ini")

    def getSections(self):
        secs = self.cf.sections()
        return secs

    def getOptions(self, section):
        options = self.cf.options(section)
        return options

    def getItems(self, section):
        items = self.cf.items(section)
        return items

    def getValue(self, section, key):
        fileName = self.cf.get(section, key)
        return fileName
