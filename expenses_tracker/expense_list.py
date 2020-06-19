from input_class import Input

class Expense_List:
    def __init__(self):
        self.expense_list = []
    
    def length(self):
        return len(self.expense_list)
    
    def list_all(self):
        out = ''
        for i in self.expense_list:
            out += i.read() + '\n'
        return out

    def add(self, x):
        self.expense_list.append(Input(x))