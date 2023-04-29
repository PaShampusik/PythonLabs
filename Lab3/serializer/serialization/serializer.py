from types import CodeType, FunctionType
from serializer.serialization.constants import *

import inspect
import re

class Serializer:

    def serialize(self, obj):
        result = {}

        if inspect.isclass(obj):
            result = self.serialize_class(obj)
            obj_type_string = CLASS_NAME
        else:
            obj_type = type(obj)
            obj_type_string = re.search(OBJECT_TYPE_REGEX, str(obj_type)).group(1)

            if obj_type == dict:
                result = self.serialize_dict(obj)
            elif isinstance(obj, (int, float, complex, bool, str, type(None))) or obj is None:
                result = self.serialize_types(obj)
            elif obj_type == list or obj_type == tuple or obj_type == bytes or obj_type == set:
                result = self.serialize_it(obj)
            elif inspect.isfunction(obj) or inspect.ismethod(obj):
                result = self.serialize_function(obj)
            elif inspect.iscode(obj) or inspect.ismethoddescriptor(obj):
                result = self.serialize_other(obj)
            elif inspect.ismodule(obj):
                result = self.serialize_module(obj)
            #elif inspect.isbuiltin(obj) and obj.__module__ is not None:
            #    result = self.serialize_builtin(obj)
            elif hasattr(obj, "__dict__"):
                result = self.serialize_object(obj)
                result[TYPE_FIELD] = OBJECT_NAME
                return FrozenDict(result)
            else:
                result = self.serialize_other(obj)

        result[TYPE_FIELD] = obj_type_string

        return frozendict(result)

    def deserialize(self, obj: dict):
        try:
            obj_type_string = obj[TYPE_FIELD]
        except:
            print("Type cannot be found!")
        result = object

        if obj_type_string == DICTIONARY_NAME:
            result = self.deserialize_dict(obj)
        elif obj_type_string in TYPES_NAMES:
            result = self.deserialize_types(obj)
        elif obj_type_string in ITERABLE_NAMES:
            result = self.deserialize_it(obj)
        elif obj_type_string == FUNCTION_NAME:
            result = self.deserialize_function(obj)
        elif obj_type_string == CLASS_NAME:
            result = self.deserialize_class(obj)
        elif obj_type_string == MODULE_NAME:
            result = self.deserialize_module(obj)
        #elif obj_type_string == BUILTIN_NAME:
        #    result = self.deserialize_builtin(obj)
        elif obj_type_string == OBJECT_NAME:
            result = self.deserialize_object(obj)
        else:
            return

        return result

    def serialize_dict(self, obj: dict):
        result = {VALUE_FIELD: {}}

        for key, value in obj.items():
            result_key = self.serialize(key)
            result_value = self.serialize(value)

            result[VALUE_FIELD][result_key] = result_value
        return result

    def deserialize_dict(self, obj):
        result = {}

        if type(obj[VALUE_FIELD]) == tuple:
            return {}

        for key, value in obj[VALUE_FIELD].items():
            result_key = self.deserialize(key)
            result_value = self.deserialize(value)
            result[result_key] = result_value

        return result

    def serialize_types(self, obj):
        result = {VALUE_FIELD: str(obj)}

        return result

    def deserialize_types(self, obj):
        result = object
        if obj[TYPE_FIELD] == TYPES_NAMES[0]:
            result = int(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[1]:
            result = float(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[2]:
            result = complex(obj[VALUE_FIELD])
        elif obj[TYPE_FIELD] == TYPES_NAMES[3]:
            result = (obj[VALUE_FIELD] == "True")
        elif obj[TYPE_FIELD] == TYPES_NAMES[5]:
            result = None
        else:
            result = obj[VALUE_FIELD]

        return result

    def serialize_it(self, obj):
        result = {VALUE_FIELD: []}

        for value in obj:
            result[VALUE_FIELD].append(self.serialize(value))

        result[VALUE_FIELD] = tuple(result[VALUE_FIELD])

        return result

    def deserialize_it(self, obj):
        result = []

        for value in obj[VALUE_FIELD]:
            result_value = self.deserialize(value)
            result.append(result_value)

        if obj[TYPE_FIELD] == ITERABLE_NAMES[0]:
            result = result
        elif obj[TYPE_FIELD] == ITERABLE_NAMES[1]:
            result = tuple(result)
        elif obj[TYPE_FIELD] == ITERABLE_NAMES[2]:
            result = bytes(result)
        elif obj[TYPE_FIELD] == ITERABLE_NAMES[3]:
            result = set(result)

        return result

    def serialize_function(self, obj):
        if inspect.ismethod(obj):
            obj = obj.__func__

        result = {VALUE_FIELD: {}}
        members = []

        for member in inspect.getmembers(obj):
            if member[0] in FUNCTION_ATTRIBUTES_NAMES:
                members.append(member)

        for key, value in members:
            result_key = self.serialize(key)
            result_value = self.serialize(value)
            result[VALUE_FIELD][result_key] = result_value

            if key == CODE_FIELD:
                global_key = self.serialize(GLOBAL_FIELD)
                result[VALUE_FIELD][global_key] = {}

                global_attributes = obj.__getattribute__(GLOBAL_FIELD)

                new_dict = dict()
                for attribute in value.__getattribute__(CO_NAMES_FIELD):

                    if attribute == obj.__name__:
                        new_dict[attribute] = obj.__name__
                    elif attribute in global_attributes:
                        if inspect.ismodule(global_attributes[attribute]) and attribute in __builtins__:
                            continue
                        new_dict[attribute] = global_attributes[attribute]

                result[VALUE_FIELD][global_key] = self.serialize(new_dict)
        return result

    def deserialize_function(self, obj):
        result = object
        function_arguments = []
        code_arguments = []
        global_arguments = {"__builtins__": __builtins__}

        for key in FUNCTION_CREATE_ATTRIBUTES_NAMES:
            value = obj[VALUE_FIELD][self.serialize(key)]

            if key == CODE_FIELD:
                for argument_key in CODE_ARGS:
                    result_argument_value = self.deserialize(obj[VALUE_FIELD][self.serialize(CODE_FIELD)]
                                                             [VALUE_FIELD][self.serialize(argument_key)])
                    code_arguments.append(result_argument_value)

                function_arguments = [CodeType(*code_arguments)]

            elif key == GLOBAL_FIELD:
                for argument_key, argument_value in self.deserialize(obj[VALUE_FIELD][self.serialize(GLOBAL_FIELD)]).items():
                    global_arguments[argument_key] = argument_value
                function_arguments.append(global_arguments)

            else:
                function_arguments.append(self.deserialize(value))

        result = FunctionType(*function_arguments)

        if result.__name__ in result.__getattribute__(GLOBAL_FIELD):
            result.__getattribute__(GLOBAL_FIELD)[result.__name__] = result

        return result

    def serialize_class(self, obj):
        result = {VALUE_FIELD: {}}
        members = []
        bases = []

        for base in obj.__bases__:
            if base.__name__ != OBJECT_NAME:
                bases.append(base)
        result[VALUE_FIELD][self.serialize(BASE_NAME)] = self.serialize(bases)

        for member in inspect.getmembers(obj):
            if member[0] not in CLASS_ATTRIBUTE_NAMES:
                members.append(member)

        result_data = self.serialize(DATA_NAME)

        new_dict = {NAME_FIELD: obj.__name__}

        for member in members:

            new_dict[member[0]] = member[1]

        result[VALUE_FIELD][result_data] = self.serialize(new_dict)

        return result

    def deserialize_class(self, obj):
        result_data = self.serialize(DATA_NAME)

        result_bases = tuple(self.deserialize(obj[VALUE_FIELD][self.serialize(BASE_NAME)]))

        result = self.deserialize(obj[VALUE_FIELD][result_data])
        result_name = result[NAME_FIELD]
        del result[NAME_FIELD]
        return type(result_name, (object,), result)

    def serialize_other(self, obj):
        result = {VALUE_FIELD: {}}
        members = []

        for member in inspect.getmembers(obj):
            if not callable(member[1]) and member[0] != DOC_ATTRIBUTE_NAME:
                members.append(member)

        for key, value in members:
            result_key = self.serialize(key)
            result_value = self.serialize(value)
            result[VALUE_FIELD][result_key] = result_value

        return result

    def deserialize_instance(self, obj):
        pass

    def serialize_module(self, obj):
        result = {VALUE_FIELD: self.serialize(obj.__name__)}
        return result

    def deserialize_module(self, obj):
        return __import__(self.deserialize(obj[VALUE_FIELD]))

    def serialize_builtin(self, obj):
        if obj.__module__ is not None:
            result = {VALUE_FIELD: self.serialize([str(obj.__module__), str(obj.__name__)])}
        else:
            result = {VALUE_FIELD: self.serialize([obj.__name__])}
        return result

    def deserialize_builtin(self, obj):
        result = self.deserialize(obj[VALUE_FIELD])
        if len(result) == 1:
            return __import__(result[0])
        else:
            return __import__(result[0], result[1])

    def serialize_object(self, obj):
        result = {VALUE_FIELD: {}}
        obj_type = type(obj)

        for attribute, value in obj.__dict__.items():
            result_attribute = self.serialize(attribute)
            result_value = self.serialize(value)
            result[VALUE_FIELD][result_attribute] = result_value

        result[VALUE_FIELD][self.serialize(TYPE_FIELD)] = self.serialize(obj_type)
        return result

    def deserialize_object(self, obj):
        result = object

        result = self.deserialize(obj[VALUE_FIELD][self.serialize(TYPE_FIELD)])()
        for attribute, value in obj[VALUE_FIELD].items():
            result_attribute = self.deserialize(attribute)
            result_value = self.deserialize(value)
            result.result_attribute = result_value

        return result