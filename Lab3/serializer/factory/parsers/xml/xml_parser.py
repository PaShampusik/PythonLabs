from serializer.factory.parsers.parser import Parser

import xml.etree.ElementTree as ET

class XmlParser(Parser):

    def dump(self, obj, file):  # obj to file
        xml_str = ET.tostring(obj.to_xml())
        with open(file, 'w') as f:
            f.write(xml_str)

    def dumps(self, obj):  # obj to string
        xml_str = ET.tostring(obj.to_xml())

        return xml_str.decode('utf-8')

    # def load(self, file):  # file to obj
    #     tree = ET.parse(file)
    #     root = tree.getroot()
    #     return MyCustomObject.from_xml(root)

    # def loads(self, string):  # string to obj
    #     return self.serializer.deserialize(yaml.load(string, Loader=UnsafeLoader))