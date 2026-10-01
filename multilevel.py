# multilevel inheritance

class Person:

    def __init__(self, name):
        self.name = name

    def show_person(self):
        print("Name:", self.name)

class Employee(Person):

    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

    def show_employee(self):
        print("Employee ID:", self.employee_id)


class Manager(Employee):

    def __init__(self, name, employee_id, department):
        super().__init__(name, employee_id)
        self.department = department

    def show_manager(self):
        print("Department:", self.department)


m1 = Manager("Ali", 101, "IT")

m1.show_person()
m1.show_employee()
m1.show_manager()