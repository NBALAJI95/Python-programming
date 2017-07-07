class Employee:
    num_employees = None

    def __init__(self, name, salary):
        if Employee.num_employees == None:
            Employee.num_employees = 0

        Employee.num_employees += 1
        self.name = name
        self.salary = salary

    def getEmployeeCount(self):
        return Employee.num_employees

    def display(self):
        print(self.name)
        print(self.salary)


class Manager(Employee):
    pass


def main():
    fresher = Employee('Jim', 2000)
    fresher1 = Employee('Jim1', 1000)
    print('Employee count', fresher1.getEmployeeCount())
    new_manager = Manager('John', 5000)
    fresher.display()
    new_manager.display()

if __name__ == '__main__':
    main()