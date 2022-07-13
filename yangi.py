import tkinter as tk
from tkinter import messagebox

def add_digit(digit):
    value = calc.get()
    if value=='0' and len(value)==1:
        value=value[1:]
    calc['state']=tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)
    calc['state'] = tk.DISABLED

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-/*':
        value=value[:-1]
    elif '+' in value or '-' in value or '/' in value or '*' in value:
        calculate()
        value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)


def make_digit_buttun(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_buttun(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=lambda: add_operation(operation))

def calculate():
    value=calc.get()
    if value[-1] in '+-/*':
        value=value+value[:-1]
    calc.delete(0, tk.END)
    try:
        calc.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("diqqat",'faqat raqamlarni kiriting!! ')
        calc.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo("diqqat", 'faqat raqamlarni kiriting, nolni nolga bolib bolmaydi!! ')
        calc.insert(0, 0)
def clear():
    calc.delete(0, tk.END)
    calc.insert(0,0)

def make_calc_buttun(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=calculate)

def make_clear_buttun(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red',
                     command=clear)

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_operation(event.char)
    elif event.char=='\r':
        calculate()

win = tk.Tk()
win.geometry(f'240x270+100+200')
win['bg'] = '#33ffe6'
win.title('kalkulyator')

#win.bind('<Key>',press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,'0')
calc['state']=tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, sticky='we',padx=5)

make_digit_buttun('1').grid(row=1, column=0, sticky='wens', padx=5, pady=5)
make_digit_buttun('2').grid(row=1, column=1, sticky='wens', padx=5, pady=5)
make_digit_buttun('3').grid(row=1, column=2, sticky='wens', padx=5, pady=5)
make_digit_buttun('4').grid(row=2, column=0, sticky='wens', padx=5, pady=5)
make_digit_buttun('5').grid(row=2, column=1, sticky='wens', padx=5, pady=5)
make_digit_buttun('6').grid(row=2, column=2, sticky='wens', padx=5, pady=5)
make_digit_buttun('7').grid(row=3, column=0, sticky='wens', padx=5, pady=5)
make_digit_buttun('8').grid(row=3, column=1, sticky='wens', padx=5, pady=5)
make_digit_buttun('9').grid(row=3, column=2, sticky='wens', padx=5, pady=5)
make_digit_buttun('0').grid(row=4, column=0, sticky='wens', padx=5, pady=5)

make_operation_buttun('+').grid(row=1, column=3, sticky='wens', padx=5, pady=5)
make_operation_buttun('-').grid(row=2, column=3, sticky='wens', padx=5, pady=5)
make_operation_buttun('/').grid(row=3, column=3, sticky='wens', padx=5, pady=5)
make_operation_buttun('*').grid(row=4, column=3, sticky='wens', padx=5, pady=5)

make_calc_buttun('=').grid(row=4, column=2, sticky='wens', padx=5, pady=5)
make_clear_buttun('C').grid(row=4, column=1, sticky='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()
