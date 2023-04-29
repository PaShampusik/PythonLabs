from serializer.factory.parsers.json.functions import *
from serializer.factory.parsers.parser import Parser

class JsonParser(Parser):

    def dump(self, obj, file):  # obj to file
        with open(file, "w") as f:
            f.write(self.dumps(obj))

    def dumps(self, obj):  # obj to string
        return to_json(self.serializer.serialize(obj))

    def load(self, file):  # file to obj
        with open(file, "r") as f:
            return self.loads(f.read())

    def loads(self, string):  # string to obj
        return self.serializer.deserialize(from_json(string))