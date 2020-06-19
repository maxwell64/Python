import PySimpleGUI as sg
import numpy as np
import matplotlib.pyplot as graph
from input_class import Input
from expense_list import Expense_List
from datetime import date

sg.theme('Dark Blue 3')

expenses = Expense_List()
f = open('Documents/pythonStuff/expenses_tracker/expenses.txt', 'a')

layout = [ [sg.Text('Welcome to the expenses tracker!')], 
[sg.Text('How much have you spent today?'), sg.InputText(key = '-IN-')],
[sg.Text('Spending appears here:\n')],
[sg.Output(key = '-OUTPUT-')],
[sg.Button('Ok'), sg.Button('Cancel'), sg.Button('Clear')] ]

window = sg.Window('Expenses Tracker', layout)

while True:
    event, values = window.read()
    inp = values['-IN-']
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'Clear':
        open('Documents/pythonStuff/expenses_tracker/expenses.txt', 'w').write('Record cleared on:', str(date.today()))
        break
    if event == 'Ok':
        expenses.add(inp)
        window['-OUTPUT-'].update(expenses.list_all())
        window['-IN-'].update('')

window.close()