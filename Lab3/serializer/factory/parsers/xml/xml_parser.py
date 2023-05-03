from functions import convert, deconvert
from constants import PRIMITIVE_TYPES
from serializer.factory.parsers.json.functions import *
from serializer.factory.parsers.parser import Parser

class Xml(Parser):
    def __init__(self):
        self._dict_counter = 0
        self._current_position = 0
        self._indent = 0

    def dumps(self, obj):
        return self._serialize_to_str(self.serializer.serialize(obj))

    def dump(self, obj, file):
        file.write(self.dumps(obj))

    def loads(self, string):
        self._current_position = 0
        return deconvert(self.serializer.deserialize(string))

    def load(self, file):
        return self.loads(file.read())