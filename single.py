#single inheritance

class Employee:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_employee(self):
        print("Employee:", self.name)
        print("Age:", self.age)

class Cashier(Employee):
    def __init__(self, name, age, salary, experience):
        super().__init__(name, age)
        self.salary = salary
        self.experience = experience

    def show_cashier(self):
        self.show_employee()
        print("Salary:", self.salary)
        print("Experience:", self.experience)

Employee1 = Cashier("Ali", 20, 60000, 2)
Employee1.show_cashier()