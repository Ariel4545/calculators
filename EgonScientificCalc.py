# imports
from tkinter import *
import math

# operation settings
multiple_numbers = ['+', '-', '*', '/', '^']

# window
root = Tk()
width = 400
height = 550
screen_width = root.winfo_width()
screen_height = root.winfo_height()
placement_x = abs((screen_width // 2) - (width // 2))
placement_y = abs((screen_height // 2) - (height // 2))
root.geometry(f'{width}x{height}+{placement_x}+{placement_y}')
root.title("Egon scientific calculator")
root.resizable(False, False)
root.configure(bg='white')


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, int(str(current) + str(number)))


def button_clear(event=None):
    entry.delete(0, END)


def button_equal(event=None):
    if operation in multiple_numbers:
        second_number = entry.get()
        entry.delete(0, END)
        s_num = int(second_number)
        # aromatics
        if operation == '+':
            entry.insert(0, f_num + s_num)
        if operation == '*':
            entry.insert(0, f_num * s_num)
        if operation == '/':
            entry.insert(0, f_num / s_num)
        if operation == '-':
            entry.insert(0, f_num - s_num)
        if operation == '^':
            entry.insert(0, pow(f_num, s_num))
    else:
        if operation == '√':
            entry.insert(0, math.sqrt(f_num))
        if operation == 'exp':
            entry.insert(0, math.exp(f_num))
        # trigonometry |
        if operation == 'sin':
            entry.insert(0, math.sin(f_num))
        if operation == 'cos':
            entry.insert(0, math.cos(f_num))
        if operation == 'tan':
            entry.insert(0, math.tan(f_num))


def op(oper):
    global operation
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)
    operation = oper


button_frame = Frame(root, padx=0)
button_frame.grid(row=1)
# creating numerical buttons
padx_b = 1
pady_b = 3
button_height = 6
button_width = 10
b1 = Button(button_frame, text="1", command=lambda: button_click(1), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b2 = Button(button_frame, text="2", command=lambda: button_click(2), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b3 = Button(button_frame, text="3", command=lambda: button_click(3), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b4 = Button(button_frame, text="4", command=lambda: button_click(4), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b5 = Button(button_frame, text="5", command=lambda: button_click(5), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b6 = Button(button_frame, text="6", command=lambda: button_click(6), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b7 = Button(button_frame, text="7", command=lambda: button_click(7), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b8 = Button(button_frame, text="8", command=lambda: button_click(8), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b9 = Button(button_frame, text="9", command=lambda: button_click(9), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b0 = Button(button_frame, text="0", command=lambda: button_click(0), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)

# placing numerical buttons
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
b3.grid(row=1, column=3)

b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
b6.grid(row=2, column=3)

b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
b9.grid(row=3, column=3)

b0.grid(row=4, column=1)

# creating operations buttons
padx_oper = padx_b
pady_oper = pady_b
equal_b = Button(button_frame, text="=", padx=padx_oper, pady=pady_oper, command=lambda: button_equal(), relief=FLAT,
                 height=button_height
                 , width=button_width)
add_b = Button(button_frame, text="+", padx=padx_oper, pady=pady_oper, command=lambda: op('+'), relief=FLAT,
               height=button_height
               , width=button_width)
sub_b = Button(button_frame, text="-", padx=padx_oper, pady=pady_oper, command=lambda: op('-'), relief=FLAT,
               height=button_height
               , width=button_width)
mul_b = Button(button_frame, text="*", padx=padx_oper, pady=pady_oper, command=lambda: op('*'), relief=FLAT,
               height=button_height
               , width=button_width)
div_b = Button(button_frame, text="÷", padx=padx_oper, pady=pady_oper, command=lambda: op('/'), relief=FLAT,
               height=button_height
               , width=button_width)
power_b = Button(button_frame, text="^", padx=padx_oper, pady=pady_oper, command=lambda: op('^'), relief=FLAT,
                 height=button_height
                 , width=button_width)
sqrt_b = Button(button_frame, text="√", padx=padx_oper, pady=pady_oper, command=lambda: op('√'), relief=FLAT,
                height=button_height
                , width=button_width)
exp_b = Button(button_frame, text="exp", padx=padx_oper, pady=pady_oper, command=lambda: op('exp'), relief=FLAT,
               height=button_height
               , width=button_width)
sin_b = Button(button_frame, text="sin", padx=padx_oper, pady=pady_oper, command=lambda: op('sin'), relief=FLAT,
               height=button_height
               , width=button_width)
cos_b = Button(button_frame, text="cos", padx=padx_oper, pady=pady_oper, command=lambda: op('cos'), relief=FLAT,
               height=button_height
               , width=button_width)
tan_b = Button(button_frame, text="tan", padx=padx_oper, pady=pady_oper, command=lambda: op('tan'), relief=FLAT,
               height=button_height
               , width=button_width)

clear_b = Button(button_frame, text="clear", padx=padx_oper, pady=pady_oper, command=lambda: button_clear(),
                 relief=FLAT,
                 height=button_height
                 , width=button_width)

# placing operations buttons
equal_b.grid(row=4, column=2)
add_b.grid(row=1, column=4)
sub_b.grid(row=2, column=4)
mul_b.grid(row=3, column=4)
div_b.grid(row=4, column=4)
power_b.grid(row=0, column=4)
sqrt_b.grid(row=0, column=1)
exp_b.grid(row=0, column=0)
sin_b.grid(row=1, column=0)
cos_b.grid(row=2, column=0)
tan_b.grid(row=3, column=0)
clear_b.grid(row=4, column=3)

# creating & placing the calculations bar
entry = Entry(root, borderwidth=2, width=40, justify=CENTER, state='normal')
entry.grid(row=0, column=0, columnspan=1, sticky=N)

# shortcuts
root.bind('<c>', button_clear)

root.mainloop()

