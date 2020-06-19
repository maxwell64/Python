from datetime import date

class Input:
    def __init__(self, amount):
        self.amount = amount
        self.date = date.today()

    def read(self):
        return '£' + str(self.amount) + ', ' + str(self.date)