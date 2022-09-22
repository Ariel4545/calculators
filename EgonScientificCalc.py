# imports
from tkinter import *
from tkinter import messagebox
import math
import random

# operation settings
multiple_numbers = ['+', '-', '*', '/', '^', 'randint']

# window
root = Tk()
width = 400
height = 540
screen_width = root.winfo_width()
screen_height = root.winfo_height()
placement_x = abs((screen_width // 2) - (width // 2))
placement_y = abs((screen_height // 2) - (height // 2))
root.geometry(f'{width}x{height}+{placement_x}+{placement_y}')
root.title("Egon scientific calculator")
root.resizable(False, False)
root.configure(bg='white')
operation_color = '#ededed'
equal_color = 'light blue'
logo = PhotoImage(file='Logo.png')
root.iconphoto(False, logo)


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
        if operation == '+':
            eq = (f_num + s_num)
        if operation == '*':
            eq = (f_num * s_num)
        if operation == '/':
            eq = (f_num / s_num)
        if operation == '-':
            eq = (f_num - s_num)
        if operation == '^':
            eq = (pow(f_num, s_num))
        if operation == 'randint':
            eq = (random.randint(f_num, s_num))
    else:
        if operation == '√':
            eq = (math.sqrt(f_num))
        if operation == 'exp':
            eq = (math.exp(f_num))
        # trigonometry |
        if operation == 'sin':
            eq = (math.sin(f_num))
        if operation == 'cos':
            eq = (math.cos(f_num))
        if operation == 'tan':
            eq = (math.tan(f_num))
        if operation == 'abs':
            eq = (abs(f_num))
        if operation == 'fact':
            eq = (math.factorial(f_num))

    entry.insert(0, eq)


def op(oper):
    global operation
    first_number = entry.get()
    global f_num
    f_num = int(first_number)
    entry.delete(0, END)
    operation = oper


def settings(event=None):
    # window
    settings_root = Toplevel()
    settings_root.resizable()
    # text and buttons for sizes
    settings_text = Label(settings_root, text='Settings', font='arial 14 bold')
    size_text = Label(settings_root, text='Size settings:', font=('arial 10 underline'), pady=5)
    size_small = Button(settings_root, text='Small')
    size_normal = Button(settings_root, text='Medium')
    size_big = Button(settings_root, text='Big')
    settings_text.grid(row=0)
    size_text.grid(row=1)
    size_small.grid(row=2, column=0)
    size_normal.grid(row=2, column=1)
    size_big.grid(row=2, column=2)
    # text and buttons for themes
    theme_text = Label(settings_root, text='Theme settings:', font='arial 10 underline', pady=5)
    theme_light = Button(settings_root, text='light theme')
    theme_dark = Button(settings_root, text='Dracula theme')
    theme_text.grid(row=3)
    theme_light.grid(row=4, column=0)
    theme_dark.grid(row=4, column=2)

    def size():
        global padx_b, pady_b
        for i in f_list:
            i.config(width=button_width, height=button_height)
        root.geometry(f'{width}x{height}')

    def small():
        global button_height, button_width
        global width, height
        button_height, button_width = 3, 6
        size_small.config(bg='grey'), size_normal.config(bg='white'), size_big.config(bg='white')
        width, height = 260, 320
        size()

    def medium():
        global button_height, button_width
        global width, height
        button_height, button_width = 6, 10
        width, height = 400, 540
        size_small.config(bg='white'), size_normal.config(bg='grey'), size_big.config(bg='white')
        size()

    def big():
        global button_height, button_width
        global width, height
        button_height, button_width = 9, 12
        width, height = 470, 740
        size_small.config(bg='white'), size_normal.config(bg='white'), size_big.config(bg='grey')
        size()

    size_small.config(command=small), size_normal.config(command=medium), size_big.config(command=big)
    medium()

    def dark_theme():
        theme_dark.config(bg='grey'), theme_light.config(bg='white')
        for i in n_list:
            i.config(bg='grey')
        for i in b_list:
            i.config(bg='dark grey')
        equal_b.config(bg='light blue')
        entry.config(bg='#373737', foreground='green')

    def light_theme():
        theme_dark.config(bg='white'), theme_light.config(bg='grey')
        for i in n_list:
            i.config(bg='SystemButtonFace')
        for i in b_list:
            i.config(bg=operation_color)
        equal_b.config(bg=equal_color)
        entry.config(bg='white', foreground='black')

    theme_dark.config(command=dark_theme), theme_light.config(command=light_theme)
    light_theme()


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
                 height=button_height, bg=equal_color
                 , width=button_width)
add_b = Button(button_frame, text="+", padx=padx_oper, pady=pady_oper, command=lambda: op('+'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
sub_b = Button(button_frame, text="-", padx=padx_oper, pady=pady_oper, command=lambda: op('-'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
mul_b = Button(button_frame, text="*", padx=padx_oper, pady=pady_oper, command=lambda: op('*'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
div_b = Button(button_frame, text="÷", padx=padx_oper, pady=pady_oper, command=lambda: op('/'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
power_b = Button(button_frame, text="^", padx=padx_oper, pady=pady_oper, command=lambda: op('^'), relief=FLAT,
                 height=button_height, bg=operation_color
                 , width=button_width)
sqrt_b = Button(button_frame, text="√", padx=padx_oper, pady=pady_oper, command=lambda: op('√'), relief=FLAT,
                height=button_height, bg=operation_color
                , width=button_width)
exp_b = Button(button_frame, text="exp", padx=padx_oper, pady=pady_oper, command=lambda: op('exp'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
sin_b = Button(button_frame, text="sin", padx=padx_oper, pady=pady_oper, command=lambda: op('sin'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
cos_b = Button(button_frame, text="cos", padx=padx_oper, pady=pady_oper, command=lambda: op('cos'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
tan_b = Button(button_frame, text="tan", padx=padx_oper, pady=pady_oper, command=lambda: op('tan'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
abs_b = Button(button_frame, text="|X|", padx=padx_oper, pady=pady_oper, command=lambda: op('abs'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
fac_b = Button(button_frame, text="!n", padx=padx_oper, pady=pady_oper, command=lambda: op('fact'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
rad_b = Button(button_frame, text="randint", padx=padx_oper, pady=pady_oper, command=lambda: op('randint'), relief=FLAT,
               height=button_height, bg=operation_color
               , width=button_width)
clear_b = Button(button_frame, text="clear", padx=padx_oper, pady=pady_oper, command=lambda: button_clear(),
                 relief=FLAT,
                 height=button_height
                 , width=button_width)
n_list = [b1, b2, b3, b4, b5, b5, b6, b7, b8, b9, b0]
b_list = [equal_b, add_b, sub_b, mul_b, div_b,  power_b, sqrt_b, exp_b, sin_b, cos_b, tan_b, abs_b, fac_b,
          rad_b, clear_b]
f_list = n_list + b_list

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
abs_b.grid(row=0, column=3)
fac_b.grid(row=0, column=2)
rad_b.grid(row=4, column=0)
clear_b.grid(row=4, column=3)

# creating & placing the calculations bar
entry = Entry(root, borderwidth=2, width=40, justify=CENTER, state='normal')
entry.grid(row=0, column=0, columnspan=1, sticky=N)

# shortcuts
root.bind('<c>', button_clear)
root.bind('<e>', lambda event: button_equal())
root.bind('<Escape>', lambda event: root.quit())
root.bind('<s>', settings)

messagebox.showinfo('Tip', 'for the settings to pop up press s')
root.mainloop()
