from PythonBasics.OopsDemo import Calculator


class ChildImpl(Calculator):
    num2 = 200

    def __init__(self):
        Calculator.__init__(self, 4, 8)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation() #call all parent class variables and methods


obj = ChildImpl()
print(obj.getCompleteData())
