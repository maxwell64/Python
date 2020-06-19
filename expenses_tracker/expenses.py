import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as graph
from input_class import Input
from expense_list import Expense_List
from datetime import date

# Defines the expenses .txt file and the theme for the window
expense_file = 'Documents/pythonStuff/expenses_tracker/expenses.txt'
sg.theme('Dark Blue 3')

# Sets up the expense list and loads previous inputs from file
expenses = Expense_List()
expenses.from_file(expense_file)
f = open('Documents/pythonStuff/expenses_tracker/expenses.txt', 'a')

# Sets the layout for the window
layout = [ [sg.Text('Welcome to the expenses tracker!')], 
[sg.Text('How much have you spent today?'), sg.InputText(key = '-IN-')],
[sg.Text('Spending appears here:')],
[sg.Output(key = '-OUTPUT-')],
[sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Clear')] ]

window = sg.Window('Expenses Tracker', layout)

while True:
    event, values = window.read()
    inp = values['-IN-']
    if event == sg.WIN_CLOSED or event == 'Cancel':
        # Breaks the loop on window close or cancel
        break
    if event == 'Clear':
        # Clears the expenses file and notes the date
        open('Documents/pythonStuff/expenses_tracker/expenses.txt', 'w').write('Record cleared on: ' + str(date.today()))
        break
    if event == 'Ok':
        # When ok button is pressed appends new expense to list and prints to file
        expenses.add(inp)
        window['-OUTPUT-'].update(expenses.list_all())
        window['-IN-'].update('')
        f.write(expenses.return_last())

window.close()