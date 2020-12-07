# Created by Leon Hunter at 9:54 AM 10/23/2020
class Calculator(object):
    def add(self, a, b):
        return a+b

    def subtract(self, a, b):
        return a-b

    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return round(a/b,3)

#print(Calculator.add(None,3.2, 4))
#print(Calculator.subtract(None,3.2, 4))
#print(Calculator.multiply(None,3.2, 4))
#print(Calculator.divide(None,3.2, 4))
#print(Calculator.divide(None,21,13))