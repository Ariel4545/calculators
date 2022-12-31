# imports
import tkinter.messagebox

import customtkinter
from customtkinter import *
from tkinter import *

# window
root = CTk()
width = 320
height = 460
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
placement_x = round((screen_width // 2) - (width // 2))
placement_y = round((screen_height // 2) - (height // 2))
root.geometry(f'{width}x{height}+{placement_x}+{placement_y}')
root.title("Egon calculator")
root.resizable(False, False)
root.configure(bg='white')
operation_color = '#e0e0e0'
equal_color = '#d5eaf2'
customtkinter.set_appearance_mode('light')
total_exp = ''

# logo = PhotoImage(file='Logo.png')
# root.iconphoto(False, logo)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear(event=None):
    entry.delete(0, END)


def button_equal(event=None):
    global total_exp
    second_number = entry.get()
    total_exp += second_number
    entry.delete(0, END)
    try:
        s_num = int(second_number)
    except ValueError:
        pass
    if operation == '+':
        entry.insert(0, f_num + s_num)
    if operation == '*':
        entry.insert(0, f_num * s_num)
    if operation == '/':
        try:
            entry.insert(0, f_num / s_num)
        except ZeroDivisionError:
            tkinter.messagebox.showerror('Error', 'Divided by zero')
    if operation == '-':
        entry.insert(0, f_num - s_num)
    total_exp_entry.configure(text=total_exp)
    total_exp.replace(total_exp, '')

def button_add():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    try:
        f_num = int(first_number)
    except ValueError:
        pass
    operation = '+'
    total_exp = f'{f_num} {operation}'
    entry.delete(0, END)


def button_sub():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    f_num = int(first_number)
    operation = '-'
    total_exp = f'{f_num} {operation}'
    entry.delete(0, END)


def button_mul():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    f_num = int(first_number)
    operation = '*'
    total_exp = f'{f_num} {operation}'
    entry.delete(0, END)


def button_div():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    f_num = int(first_number)
    operation = '/'
    total_exp = f'{f_num} {operation}'
    entry.delete(0, END)


equation = StringVar()
expression = ''


def aio_clac(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        total_exp_entry.configure(text=expression)
        expression = total
    except:
        equation.set(" error ")
        expression = ""

def aio_clear():
    global expression
    expression = ""
    equation.set("")

def settings(event=None):
    # window
    settings_root = CTkToplevel()
    settings_root.title('')
    settings_text = CTkLabel(settings_root, text='Settings')
    btn_width = 5

    def size():
        global padx_b, pady_b
        for i in f_list:
            i.config(padx=padx_b, pady=pady_b)
        root.geometry(f'{width}x{height}')
        entry.config(width=get_entry_width())

    def small():
        global padx_b, pady_b
        global width, height
        padx_b, pady_b = 1, 3
        width, height = 320, 430 + 30
        size()

    def medium():
        global padx_b, pady_b
        global width, height
        padx_b, pady_b = 2, 6
        width, height = 355, 455 + 30
        size()

    def big():
        global padx_b, pady_b
        global width, height
        padx_b, pady_b = 4, 12
        width, height = 370, 500 + 30
        size()

    # text and buttons for sizes
    size_text = CTkLabel(settings_root, text='Size settings:', pady=5)
    size_small = CTkButton(settings_root, text='Small', command=small, width=btn_width)
    size_normal = CTkButton(settings_root, text='Medium', command=medium, width=btn_width)
    size_big = CTkButton(settings_root, text='Big', command=big, width=btn_width)
    small()

    def dark_theme():
        for i in n_list:
            i.config(bg='#222623', foreground='dark green')
        for i in b_list:
            i.config(bg='#454545', fg='white')
        equal_b.config(bg='dark blue')
        entry.config(bg='#373737', foreground='green')
        total_exp_entry.config(bg='#373737', foreground='green')
        customtkinter.set_appearance_mode('dark')

    def light_theme():
        for i in n_list:
            i.config(bg='SystemButtonFace', foreground='black')
        for i in b_list:
            i.config(bg=operation_color, foreground='black')
        equal_b.config(bg=equal_color)
        entry.config(bg='white', foreground='black')
        total_exp_entry.config(bg='white', foreground='black')
        customtkinter.set_appearance_mode('light')

    # text and buttons for themes
    theme_text = CTkLabel(settings_root, text='Theme settings:', pady=5)
    theme_light = CTkButton(settings_root, text='light theme', command=light_theme, width=btn_width)
    theme_dark = CTkButton(settings_root, text='Dracula theme', command=dark_theme, width=btn_width)
    light_theme()

    def change_c(mode):
        if mode == 'one':
            for i in range(len(n_list)):
                n_list[i].config(command=lambda i=i: button_click(i))
            div_b.configure(command=button_div), mul_b.configure(command=button_mul),\
            add_b.configure(command=button_add), sub_b.configure(command=button_sub),\
            clear_b.configure(command=button_clear)
            equal_b.configure(command=button_equal)
            entry.configure(textvariable=None)
        else:
            for i, button in enumerate(n_list):
                button.configure(command=lambda i=i: aio_clac(i))
            div_b.configure(command=lambda: aio_clac('/')), mul_b.configure(command=lambda: aio_clac('*'))\
                , add_b.configure(command=lambda: aio_clac('+')), sub_b.configure(command=lambda: aio_clac('-'))\
                , clear_b.configure(command=aio_clear)
            equal_b.configure(command=equalpress)
            entry.configure(textvariable=equation)

    # calculation modes
    calculation_text = CTkLabel(settings_root, text='calculation settings:', pady=5)
    one_at_a_time = CTkButton(settings_root, text='one at a time', command=lambda: change_c('one'), width=btn_width)
    everything_at_once = CTkButton(settings_root, text='everything at once', command=lambda: change_c('everything')
                                   , width=btn_width)

    # placing
    settings_text.grid(row=0)
    size_text.grid(row=1)
    size_small.grid(row=2, column=0)
    size_normal.grid(row=2, column=1)
    size_big.grid(row=2, column=2)
    theme_text.grid(row=3)
    theme_light.grid(row=4, column=0)
    theme_dark.grid(row=4, column=1)

    calculation_text.grid(row=5, column=1)
    one_at_a_time.grid(row=6, column=0)
    everything_at_once.grid(row=6, column=2)


def get_entry_width():
    return (width // 8) - 10


# frames
entry_frame = Frame(root)
entry_frame.pack()
button_frame = Frame(root, padx=0)
button_frame.pack(fill=X)
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
b3 = Button(button_frame, text="3", command=lambda: button_click(3), pady=pady_b, relief=FLAT,
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
b7 = Button(button_frame, text="7", command=lambda: button_click(7), pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b8 = Button(button_frame, text="8", command=lambda: button_click(8), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b9 = Button(button_frame, text="9", command=lambda: button_click(9), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
b0 = Button(button_frame, text="0", command=lambda: button_click(0), pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)

n_list = [b0, b1, b2, b3, b4, b5, b6, b7, b8, b9]

# placing numerical buttons
b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)

b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)

b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)

b0.grid(row=4, column=0)

# creating operations buttons
padx_oper = padx_b
pady_oper = pady_b
equal_b = Button(button_frame, text="=", padx=padx_oper, pady=pady_oper, command=lambda: button_equal(), relief=FLAT,
                 height=button_height, bg=equal_color
                 , width=button_width)
add_b = Button(button_frame, text="+", padx=padx_oper, pady=pady_oper, command=lambda: button_add(), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
sub_b = Button(button_frame, text="-", padx=padx_oper, pady=pady_oper, command=lambda: button_sub(), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
mul_b = Button(button_frame, text="*", padx=padx_oper, pady=pady_oper, command=lambda: button_mul(), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
div_b = Button(button_frame, text="/", padx=padx_oper, pady=pady_oper, command=lambda: button_div(), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
clear_b = Button(button_frame, text="X", padx=padx_oper, pady=pady_oper, command=lambda: button_clear(), relief=FLAT,
                 height=button_height, bg=operation_color
                 , width=button_width)
b_list = [equal_b, add_b, sub_b, mul_b, div_b, clear_b]
f_list = n_list + b_list
# placing operations buttons
equal_b.grid(row=4, column=1)
add_b.grid(row=1, column=4)
sub_b.grid(row=2, column=4)
mul_b.grid(row=3, column=4)
div_b.grid(row=4, column=4)
clear_b.grid(row=4, column=2)

# creating & placing the calculations bar
total_exp_entry = Label(entry_frame, width=get_entry_width()//2, text=total_exp, anchor=NE, padx=10, justify=CENTER)
entry = Entry(entry_frame, borderwidth=2, width=get_entry_width(), justify=CENTER, state='normal')
total_exp_entry.pack(expand=True, fill=BOTH, anchor=N)
entry.pack(anchor=N)

# shortcuts
root.bind('<Key-c>', button_clear)
root.bind('<Key-e>', lambda event: button_equal())
# root.bind('<1>', lambda event: button_click(1))
root.bind('<Escape>', lambda event: root.quit())
root.bind('<Key-s>', lambda event: settings())
root.bind('<Key-S>', lambda event: settings())

tkinter.messagebox.showinfo('Tip', 'for the settings to pop up press s')
root.mainloop()
