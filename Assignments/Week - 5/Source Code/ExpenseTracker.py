# Classes: # ExpenseManager, Transaction, # Bank Account, # User, # Income


class Income:
    def __init__(self, monthly_income=-1):
        self.monthly_income = monthly_income

    def update_income(self, income):
        self.monthly_income = income

    def update_raise(self, perc):
        self.monthly_income = self.monthly_income + self.monthly_income * perc / 100

    def update_cut(self, perc):
        self.monthly_income = self.monthly_income - self.monthly_income * perc / 100


class BankAccount:
    def __init__(self, username):
        self.userName = username
        self.__PIN = None

    def set_PIN(self, val):
        self.__PIN = val

    def authenticate(self, uname, pin):
        if self.userName == uname and self.__PIN == pin:
            return True
        else:
            return False


class User:
    def __init__(self, name = '', age = -1):
        self.name = name
        self.age = age
        self.b = None
        self.income = Income(float(input('Enter your monthly income:')))

    def get_details(self):
        print(self.name, self.age)

    def manage_bank_account(self):
        u_name = input('Enter UserName of your bank account:')
        self.b = BankAccount(u_name)
        psw = int(input('Set PIN for your Bank Account:'))
        self.b.set_PIN(psw)


class Transaction:
    def __init__(self):
        self.expenseList = list()

    def add_expense(self, label='', type='', time=-1, amt = 0):
        new_expense = dict()
        new_expense['Label'] = label
        new_expense['Type'] = type
        new_expense['Timestamp'] = time
        new_expense['Amount'] = amt
        self.expenseList.append(new_expense)

    def remove_last_expense(self):
        del self.expenseList[-1]


class ExpenseManager(Transaction):
    def __init__(self):
        super(ExpenseManager, self).__init__()
        self.user = None

    def display_expenses(self):
        for expense in self.expenseList:
            for key in expense.keys():
                print(key+': '+str(expense[key]))

    def login(self, user):
        self.user = user
        usr = input('Enter UserName:')
        psw = int(input('Enter PIN:'))

        if user.b.authenticate(usr, psw):
            print('Logged in...')
        else:
            print('Authentication fail')

    def expense_summary(self):
        total = 0
        for expense in self.expenseList:
           total += expense['Amount']
        print('Total Expenses:', total)
        print('\n\nBudget left:', self.user.income.monthly_income - total)

def main():
    e = ExpenseManager()
    t = input("Enter user name and age separated by commma: ").split(',')
    new_user = User(t[0], t[1])
    new_user.manage_bank_account()

    e.login(new_user)
    while True:
        exp = input('Do you want to add expense?')
        if exp[0].lower()=='n':
            break
        else:
            l = input('Enter name of the expense:')
            ty = input('Enter type of the expense:')
            ti = float(input('Enter timestamp of the expense:'))
            e.add_expense(l, ty, ti, float(input('Enter Amount:')))
            rm = input('Do you want to remove the newly added expense?')
            if rm[0].lower() == 'y':
                e.remove_last_expense()
    print('\n##### Expenses #####\n')
    e.display_expenses()
    print('\n\n')
    e.expense_summary()
    print('Thank you for using...\nHave a great day!')

if __name__ == '__main__':
    main()