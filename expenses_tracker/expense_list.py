from input_class import Input
from datetime import datetime

class Expense_List:
    # Class to contain a list of expense inputs and neatly access them
    def __init__(self):
        self.expense_list = []
    
    def length(self):
        # Returns the number of expense inputs
        return len(self.expense_list)
    
    def list_all(self):
        # Lists all expenses as a single string
        out = ''
        for i in self.expense_list:
            out += i.read() + '\n'
        return out

    def return_last(self):
        # Returns the last expense input (for showing in window)
        return self.expense_list[-1].read() + '\n'

    def add(self, x):
        # Adds a new expense input
        self.expense_list.append(Input(x))

    def from_file(self, file):
        # Loads previous expenses from a specified .txt file
        f = open(str(file), 'r')
        lines = f.read().split('\n')
        for i in lines[1:-1]:
            i = i.split(', ')
            temp = Input(float(i[0][1:]))
            temp.date = datetime.strptime(i[1], '%Y-%m-%d').date()
            temp.currency = i[0][0]
            self.expense_list.append(temp)

