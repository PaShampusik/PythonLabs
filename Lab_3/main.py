from serializers.json_serializer.JsonSerializer import JsonSerializer
from serializers.xml_serializer.XmlSerializer import XmlSerializer

while (True):
    print('1: deserialize from json')
    print('2: deserialize from xml')
    print('3: json to xml')
    print('4: xml to json')

    choice = input()
    match choice:
        case '1':
            file_name = input('Input file name: ')
            with open(file_name, 'r') as f:
                print(JsonSerializer.load(f))

        case '2':
            file_name = input("input file name: ")
            with open(file_name, 'r') as f:
                print(XmlSerializer.load(f))

        case '3':
            file_name = input("input json file name: ")
            xml = input('input xml file name: ')
            with open(file_name, 'r') as f:
                obj = JsonSerializer.load(f)
            with open(xml, 'w', encoding='utf-8') as f:
                XmlSerializer.dump(obj, f)

        case '4':
            file_name = input("input xml file name: ")
            json = input('input json file name: ')
            with open(file_name, 'r') as f:
                obj = XmlSerializer.load(f)
            with open(json, 'w', encoding='utf-8') as f:
                JsonSerializer.dump(obj, f)

        case "exit()":
            exit()
        case _:
            print('incorrect')
