import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg="#17161b")

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)

def clear():
    global equation 
    equation = ""
    label_result.config(text="0")

def calculate():
    global equation
    result = "0"
    if equation != "":
        try:
            result = str(eval(equation))
        except:
            result = "Error"
            equation = ""
    label_result.config(text=result)
    equation = result

def backspace():
    global equation
    if equation:
        equation = equation[:-1]
        label_result.config(text=equation if equation else "0")

label_result = Label(root, width=20, height=2, text="0", font=("arial", 35), 
                    bg="#17161b", fg="white", anchor="e", justify=RIGHT)
label_result.pack(pady=20)

button_frame = Frame(root, bg="#17161b")
button_frame.pack()

buttons = [
    ['C', '⌫', '%', '/'],
    ['7', '8', '9', '*'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+'],
    ['0', '.', '=']
]

button_config = {
    'C': {'bg': '#3697f5', 'fg': '#fff'},
    '⌫': {'bg': '#ff6b6b', 'fg': '#fff'},
    '=': {'bg': "#106a06", 'fg': '#fff'},
    'default': {'bg': '#2a2d36', 'fg': '#fff'}
}

def get_button_config(text):
    return button_config.get(text, button_config['default'])

row, col = 0, 0
for r, row_buttons in enumerate(buttons):
    for c, text in enumerate(row_buttons):
        if text == '0':
            btn = Button(button_frame, text=text, width=11, height=1, 
                        font=("arial", 25, "bold"), bd=1, relief="flat",
                        **get_button_config(text))
            btn.grid(row=r, column=c, columnspan=2, padx=5, pady=5, sticky="ew")
            col += 1
        elif text == '=':
            btn = Button(button_frame, text=text, width=5, height=3, 
                        font=("arial", 25, "bold"), bd=1, relief="flat",
                        **get_button_config(text))
            btn.grid(row=r, column=c, rowspan=2, padx=5, pady=5, sticky="nsew")
        else:
            btn = Button(button_frame, text=text, width=5, height=1, 
                        font=("arial", 25, "bold"), bd=1, relief="flat",
                        **get_button_config(text))
            btn.grid(row=r, column=c, padx=5, pady=5, sticky="ew")
        
        if text == 'C':
            btn.config(command=clear)
        elif text == '⌫':
            btn.config(command=backspace)
        elif text == '=':
            btn.config(command=calculate)
        else:
            btn.config(command=lambda t=text: show(t))

for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)

root.bind('<Key>', lambda e: handle_keypress(e))
root.bind('<Return>', lambda e: calculate())
root.bind('<BackSpace>', lambda e: backspace())
root.bind('<Escape>', lambda e: clear())

def handle_keypress(event):
    key = event.char
    if key in '0123456789':
        show(key)
    elif key in '+-*/.%':
        show(key)
    elif key in '\r':
        calculate()

root.focus_set()
root.mainloop()