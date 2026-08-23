#classes are user defined blurprint or prototype
# class contains : methods, class variable, instance variable, constructor etc
# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose
# constructor name should be __init__
# new keyword is not required when you create object

class Calculator:
    num = 100   #class variable

    #default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")

    def getData(self):
        print("i am now executing as method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2,3)  #syntax to create objects in python
obj.getData()
print(obj.num)

obj1 = Calculator(4,5)  #syntax to create objects in python
obj1.getData()
print(obj1.Summation())

