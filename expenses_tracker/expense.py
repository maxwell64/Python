from datetime import date

class Expense:
    # Class to contain information about an expense input
    def __init__(self, amount):
        self.amount = float(amount)
        self.date = date.today()
        self.currency = '£'

    def read(self):
        # Returns the details of the input as a string
        return self.currency + str(self.amount) + ', ' + str(self.date)