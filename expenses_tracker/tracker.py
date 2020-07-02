import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as graph
import sqlite3
from sqlite3 import Error, Connection
from expense import Expense
from expense_list import Expense_List
import database
from datetime import date

# Defines the expenses database file and the theme for the window
expense_file = 'Documents/pythonStuff/expenses_tracker/expenses.db'
sg.theme('Dark Blue 3')

# Creates and/or connects to the expenses database
conn = database.make_connection(expense_file)
database.connect_expense_db(conn)

# Sets up the expense list and loads previous inputs from file
expenses = Expense_List()
expenses.from_file(expense_file, conn)

# Sets the layout for the window
layout = [ [sg.Text('Welcome to the expenses tracker!')], 
[sg.Text('How much have you spent today?'), sg.DropDown(('£', '$'), key = '-CURRENCY-'), sg.InputText(size = (10,10), key = '-IN-', do_not_clear = False)],
[sg.Text('Spending appears here:')],
[sg.Multiline(size = (40, 20), key = '-OUTPUT-')],
[sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Clear')] ]

# Sets up the PySimpleGUI window
window = sg.Window('Expenses Tracker', layout)

while True:
    event, values = window.read()
    inp = values['-IN-']
    currency = str(values['-CURRENCY-'])
    window['-OUTPUT-'].update(expenses.list_all())
    if event == sg.WIN_CLOSED or event == 'Cancel':
        # Breaks the loop on window close or cancel
        break
    if event == 'Clear':
        # Clears the expenses file and notes the date
        if sg.popup_yes_no('Are you sure?') == 'Yes':
            database.delete_all(conn)
            break
    if event == 'Ok':
        # When ok button is pressed appends new expense to list and adds to database
        if inp != '':
            expenses.add(inp)
            '''
            Currency menu bug causes inputs to not save to file
            if values['-CURRENCY-'] != '':
                expenses.set_currency(-1, currency)
            '''
            database.insert_expense(conn, expenses.get(-1))
            window['-OUTPUT-'].update(expenses.list_all())

# Closes the window after the loop is broken
window.close()