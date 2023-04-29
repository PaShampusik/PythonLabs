from serializer.factory.parsers.constants import *
from serializer.factory.parsers.json.json_parser import JsonParser
from serializer.factory.parsers.xml.xml_parser import XmlParser
from serializer.factory.parsers.yaml.yaml_parser import YamlParser

class Factory(object):

    @staticmethod
    def get_parser(pars_type: str):
        if pars_type.__eq__(JSON_NAME):
            return JsonParser()
        elif pars_type.__eq__(XML_NAME):
            return XmlParser()
        elif pars_type.__eq__(YAML_NAME):
            return YamlParser()
        else:
            return YamlParser()