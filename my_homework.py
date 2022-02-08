class Homework:
    number1 = 15
    number2 = 25

    def __init__(self,sales,price):
        self.sales = sales
        self.price = price

    def my_firstfunc(self):
        self.epickphrase = 'holly shit'
        print(self.epickphrase)

    def my_seconfunc(self):
        return self.number1 + self.number2

    def my_thirdfunc(self):
        return self.sales * self.price

my_homework = Homework(15,10)
print(my_homework.number1,my_homework.number2)
print(my_homework.my_seconfunc())
print(my_homework.my_thirdfunc())
my_homework.my_firstfunc()