class Calculator:
    num = 100

    def __init__(self, a, b):
        self.firstNumber = a
        self.secondNumber = b
        print("i am default constructor, called automatically when object is created in class")

    def getData(self):
        print("method of a class")

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Calculator(2, 4)
print(obj.summation())
