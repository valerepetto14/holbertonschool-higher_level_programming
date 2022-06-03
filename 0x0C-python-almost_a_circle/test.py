import json

string = '{"nombre": "valentin"}'

obj = json.loads(string)
print(type(obj))
string = json.dumps(obj)
print(type(string))


def suma(a,b):
        """
        It takes two numbers as input and returns their sum
        
        :param a: The first number to add
        :param b: The second number to add
        :return: The sum of a and b
        """
        return a + b