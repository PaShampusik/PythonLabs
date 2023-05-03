from test_data import *
from serializer.factory.factory import Factory

JSON_PATH = "files/JSON.json"
XML_PATH = "files/XML.xml"

def test_simples(parser="json"):
    parser = Factory.get_parser(parser)
    simples = [test_int, test_float, test_complex, test_bool, test_str, test_none]
    for simple in simples:
        parser.dump(simple, JSON_PATH)
        
        assert simple == parser.load(JSON_PATH)


def test_iterables(parser="json"):
    parser = Factory.get_parser(parser)
    iterables = [test_list, test_tuple, test_complex, test_set, test_dict]
    for iterable in iterables:
        assert iterable == parser.loads(parser.dumps(iterable))

def test_functions(parser="json"):
    parser = Factory.get_parser(parser)
    functions = [function_factorial_test, function_sum_test, function_abs_test, function_ref_test, function_sin_test]
    for function in functions:
        parser.dump(function, JSON_PATH)

        assert function(5) == parser.load(JSON_PATH)(5)


def test_lambdas(parser="json"):
    parser = Factory.get_parser(parser)

    assert lambda_test(4) == parser.loads(parser.dumps(lambda_test))(4)


def test_classes(parser="json"):
    parser = Factory.get_parser(parser)
    classes = [Car, OldCar]
    for cls in classes:
        parser.dump(cls, JSON_PATH)
        assert cls.model == parser.load(JSON_PATH).model
    car_orig = Car()
    car_ser = parser.loads(parser.dumps(Car))()

    assert car_orig.get_info() == car_ser.get_info()

a  = A()

def test_objects(parser="json"):
    parser = Factory.get_parser(parser)
    car_orig = Car(5000, "White")
    car_ser = parser.loads(parser.dumps(car_orig))
    assert car_orig.meth() == car_ser.meth()
    assert car_orig.get_color() == car_ser.get_color()
    assert car_orig.get_info() == car_ser.get_info()

    fake_a = parser.loads(parser.dumps(a))

    assert a.meth() == fake_a.meth()


#----XML----#

def test_simples(parser="xml"):
    parser = Factory.get_parser(parser)
    simples = [test_int, test_float, test_complex, test_bool, test_str, test_none]
    for simple in simples:
        parser.dump(simple, XML_PATH)
        assert simple == parser.load(XML_PATH)


def test_iterables(parser="xml"):
    parser = Factory.get_parser(parser)
    iterables = [test_list, test_tuple, test_complex, test_set, test_dict]
    for iterable in iterables:
        assert iterable == parser.loads(parser.dumps(iterable))

def test_functions(parser="xml"):
    parser = Factory.get_parser(parser)
    functions = [function_factorial_test, function_sum_test, function_abs_test, function_ref_test, function_sin_test]
    for function in functions:
        parser.dump(function, XML_PATH)

        assert function(5) == parser.load(XML_PATH)(5)


def test_lambdas(parser="xml"):
    parser = Factory.get_parser(parser)

    assert lambda_test(4) == parser.loads(parser.dumps(lambda_test))(4)


def test_classes(parser="xml"):
    parser = Factory.get_parser(parser)
    classes = [Car, OldCar]
    for cls in classes:
        parser.dump(cls, XML_PATH)
        assert cls.model == parser.load(XML_PATH).model
    car_orig = Car()
    car_ser = parser.loads(parser.dumps(Car))()

    assert car_orig.get_info() == car_ser.get_info()

a  = A()

def test_objects(parser="xml"):
    parser = Factory.get_parser(parser)
    car_orig = Car(5000, "White")
    car_ser = parser.loads(parser.dumps(car_orig))
    assert car_orig.meth() == car_ser.meth()
    assert car_orig.get_color() == car_ser.get_color()
    assert car_orig.get_info() == car_ser.get_info()

    fake_a = parser.loads(parser.dumps(a))
    assert a.meth() == fake_a.meth()