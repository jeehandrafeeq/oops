#Hierarchical inheritance
class Employee:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Employee Name:", self.name)


class Manager(Employee):

    def manager_work(self):
        print(self.name, "manages the team")


class Developer(Employee):

    def developer_work(self):
        print(self.name, "writes code")



m1 = Manager("Ali")
d1 = Developer("Ahmed")

m1.show_name()
d1.show_name()

m1.manager_work()
d1.developer_work()