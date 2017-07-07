class Employee:
    num_employees = 0

    def __init__(self, name, salary):
        self.num_employees += 1
        self.name = name
        self.salary = salary

    def getEmployeeCount(self):
        return self.num_employees

    def display(self):
        print(self.name)
        print(self.salary)


class Manager(Employee):
    pass


def main():
    fresher = Employee('Jim', 2000)
    new_manager = Manager('John', 5000)
    print('Employee count', fresher.getEmployeeCount())
    fresher.display()
    new_manager.display()

if __name__ == '__main__':
    main()