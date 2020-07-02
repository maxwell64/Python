from expense import Expense
from datetime import datetime
import database

class Expense_List:
    # Class to contain a list of expense inputs and neatly access them
    def __init__(self):
        self.expense_list = []
    
    def length(self):
        # Returns the number of expense Expenses
        return len(self.expense_list)
    
    def list_all(self):
        # Lists all expenses as a single string
        out = ''
        for i in self.expense_list:
            out += i.read() + '\n'
        return out

    def return_last(self):
        # Returns the last expense input (for printing to file)
        return self.get(-1).read() + '\n'

    def add(self, x):
        # Adds a new expense input
        self.expense_list.append(Expense(x))

    def from_file(self, file, conn):
        # Loads previous expenses from a specified .txt file
        expenses = database.fetch_all(conn)
        for i in expenses:
            temp = Expense(i[2])
            temp.date = datetime.strptime(i[3], '%Y-%m-%d').date()
            temp.currency = i[1]
            self.expense_list.append(temp)

    def get(self, index):
        # Returns the specified value
        return self.expense_list[index]

    def set_currency(self, index, c):
        # Sets the currency of the specified value
        self.expense_list[index].currency = c

    def total(self):
        total = 0
        for i in self.expense_list:
            total += i.amount
        return total
