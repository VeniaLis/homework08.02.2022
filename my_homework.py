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

class Сalculator:
    def __init__(self):
        self.my_func()

    def my_func(self):
        self.number1 = int(input('Введите число: '))
        self.number2 = int(input('Введите число: '))

    def my_func1(self):
        return self.number1 + self.number2

    def my_func2(self):
        return self.number1 - self.number2

    def my_func3(self):
        return self.number1 * self.number2

    def my_func4(self):
        if self.number2 == 0:
            return 'Так делать нельзя'
        else:
            return self.number1 / self.number2

while True:
    signs = input('Введите (+,-,*,/): ')

    example = Сalculator()
    if signs == '+':
        print(example.my_func1())
    elif signs == '-':
        print(example.my_func2())
    elif signs == '*':
        print(example.my_func3())
    elif signs == '/':
        print(example.my_func4())