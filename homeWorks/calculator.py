class Calculator:
    def __init__(self, x):
        self.x = x
    #
    def __add__(self, other):
        return self.x + other

    def __sub__(self, other):
        return self.x - other

    def __mul__(self, other):
        return self.x * other

    def __truediv__(self, other):
        if other != 0:
            return self.x / other
        else:
            return 'devision by zero is not allowed'

a = Calculator(7)
print(a+7)
print(a-7)
print(a*7)
print(a/7)