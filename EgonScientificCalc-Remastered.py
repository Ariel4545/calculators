# imports
from tkinter import *
import customtkinter
from customtkinter import *
from tkinter import messagebox
import math
import random

# operation settings
multiple_numbers = ['+', '-', '*', '/', '^', 'randint']

# window
root = CTk()
width = 400
height = 570
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
placement_x = abs((screen_width // 2) - (width // 2))
placement_y = abs((screen_height // 2) - (height // 2))
root.geometry(f'{width}x{height}+{placement_x}+{placement_y}')
root.title("Egon scientific calculator")
root.resizable(False, False)
root.configure(bg='white')
operation_color = '#ededed'
equal_color = 'light blue'
set_appearance_mode('light')

total_exp = ''
equation = StringVar()
expression = ''
calc_mode = 'one'
operation = None
f_num = 0

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, int(str(current) + str(number)))


def button_clear(event=None):
    entry.delete(0, END)


def button_equal(event=None):
    global total_exp
    if operation is None:
        return
    if operation in multiple_numbers:
        second_number = entry.get()
        total_exp += second_number
        entry.delete(0, END)
        try:
            s_num = int(second_number)
            if operation == '+':
                eq = (f_num + s_num)
            if operation == '*':
                eq = (f_num * s_num)
            if operation == '/':
                try:
                    eq = (f_num / s_num)
                except ZeroDivisionError:
                    messagebox.showerror('Error', 'Divided by zero')
            if operation == '-':
                eq = (f_num - s_num)
            if operation == '^':
                eq = (pow(f_num, s_num))
            if operation == 'randint':
                eq = (random.randint(f_num, s_num))
            entry.insert(0, eq)
        except ValueError:
            pass
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
        try:
            entry.insert(0, eq)
        except:
            pass
    total_exp_entry.configure(text=total_exp)
    total_exp = ''


def op(oper):
    global operation
    first_number = entry.get()
    global f_num
    global total_exp
    try:
        f_num = int(first_number)
    except ValueError:
        f_num = 0
    entry.delete(0, END)
    operation = oper
    if oper in multiple_numbers:
        total_exp = f'{f_num} {operation} '
    else:
        total_exp = f'{operation}({f_num})'
        total_exp_entry.configure(text=total_exp)


def aio_clac(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equalpress():
    try:
        global expression
        safe_expression = expression.replace('^', '**').replace('÷', '/')
        total = str(eval(safe_expression))
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
    settings_root.title('Settings')
    settings_root.geometry('400x300')
    settings_text = CTkLabel(settings_root, text='Settings', font=("Arial", 16, "bold"))
    btn_width = 80

    def size():
        global padx_b, pady_b
        for i in f_list:
            i.configure(width=button_width, height=button_height)
        root.geometry(f'{width}x{height}')
        entry.configure(width=get_width())

    def small():
        global button_height, button_width
        global width, height
        button_height, button_width = 3, 6
        width, height = 260, 320 + 30
        size()
        update_size_buttons('small')

    def medium():
        global button_height, button_width
        global width, height
        button_height, button_width = 6, 10
        width, height = 400, 540 + 30
        size()
        update_size_buttons('medium')

    def big():
        global button_height, button_width
        global width, height
        button_height, button_width = 9, 12
        width, height = 470, 740 + 30
        size()
        update_size_buttons('big')

    def update_size_buttons(active_size):
        buttons = {'small': size_small, 'medium': size_normal, 'big': size_big}
        for name, btn in buttons.items():
            if name == active_size:
                btn.configure(fg_color=("#3B8ED0", "#1F6AA5"))
            else:
                btn.configure(fg_color=("gray75", "gray25"))

    def dark_theme():
        # Dark Theme Colors
        bg_color = '#1e1e1e'
        btn_num_bg = '#333333'
        btn_op_bg = '#4a4a4a'
        text_color = 'white'
        
        root.configure(bg=bg_color)
        entry_frame.configure(bg=bg_color)
        button_frame.configure(bg=bg_color)
        
        for i in n_list:
            i.configure(bg=btn_num_bg, fg=text_color)
        for i in b_list:
            i.configure(bg=btn_op_bg, fg=text_color)
        equal_b.configure(bg='#005f73', fg='white')
        entry.configure(bg='#2b2b2b', foreground='white', insertbackground='white')
        total_exp_entry.configure(bg=bg_color, foreground='gray')
        
        set_appearance_mode('dark')
        update_theme_buttons('dark')

    def light_theme():
        # Light Theme Colors
        bg_color = 'white'
        
        root.configure(bg=bg_color)
        entry_frame.configure(bg=bg_color)
        button_frame.configure(bg=bg_color)
        
        for i in n_list:
            i.configure(bg='SystemButtonFace', fg='black')
        for i in b_list:
            i.configure(bg=operation_color, fg='black')
        equal_b.configure(bg=equal_color, fg='black')
        entry.configure(bg='white', foreground='black', insertbackground='black')
        total_exp_entry.configure(bg='white', foreground='gray')
        
        set_appearance_mode('light')
        update_theme_buttons('light')

    def update_theme_buttons(active_theme):
        if active_theme == 'light':
            theme_light.configure(fg_color=("#3B8ED0", "#1F6AA5"))
            theme_dark.configure(fg_color=("gray75", "gray25"))
        else:
            theme_light.configure(fg_color=("gray75", "gray25"))
            theme_dark.configure(fg_color=("#3B8ED0", "#1F6AA5"))

    def change_c(mode):
        global calc_mode
        calc_mode = mode
        if mode == 'one':
            b1.configure(command=lambda: button_click(1))
            b2.configure(command=lambda: button_click(2))
            b3.configure(command=lambda: button_click(3))
            b4.configure(command=lambda: button_click(4))
            b5.configure(command=lambda: button_click(5))
            b6.configure(command=lambda: button_click(6))
            b7.configure(command=lambda: button_click(7))
            b8.configure(command=lambda: button_click(8))
            b9.configure(command=lambda: button_click(9))
            b0.configure(command=lambda: button_click(0))
            
            add_b.configure(command=lambda: op('+'))
            sub_b.configure(command=lambda: op('-'))
            mul_b.configure(command=lambda: op('*'))
            div_b.configure(command=lambda: op('/'))
            power_b.configure(command=lambda: op('^'))
            sqrt_b.configure(command=lambda: op('√'))
            exp_b.configure(command=lambda: op('exp'))
            sin_b.configure(command=lambda: op('sin'))
            cos_b.configure(command=lambda: op('cos'))
            tan_b.configure(command=lambda: op('tan'))
            abs_b.configure(command=lambda: op('abs'))
            fac_b.configure(command=lambda: op('fact'))
            rad_b.configure(command=lambda: op('randint'))
            clear_b.configure(command=button_clear)
            equal_b.configure(command=button_equal)
            entry.configure(textvariable=None)
            
            one_at_a_time.configure(fg_color=("#3B8ED0", "#1F6AA5"))
            everything_at_once.configure(fg_color=("gray75", "gray25"))
        else:
            b1.configure(command=lambda: aio_clac(1))
            b2.configure(command=lambda: aio_clac(2))
            b3.configure(command=lambda: aio_clac(3))
            b4.configure(command=lambda: aio_clac(4))
            b5.configure(command=lambda: aio_clac(5))
            b6.configure(command=lambda: aio_clac(6))
            b7.configure(command=lambda: aio_clac(7))
            b8.configure(command=lambda: aio_clac(8))
            b9.configure(command=lambda: aio_clac(9))
            b0.configure(command=lambda: aio_clac(0))

            add_b.configure(command=lambda: aio_clac('+'))
            sub_b.configure(command=lambda: aio_clac('-'))
            mul_b.configure(command=lambda: aio_clac('*'))
            div_b.configure(command=lambda: aio_clac('÷'))
            power_b.configure(command=lambda: aio_clac('^'))
            
            # Scientific functions for AIO
            sqrt_b.configure(command=lambda: aio_clac('math.sqrt('))
            exp_b.configure(command=lambda: aio_clac('math.exp('))
            sin_b.configure(command=lambda: aio_clac('math.sin('))
            cos_b.configure(command=lambda: aio_clac('math.cos('))
            tan_b.configure(command=lambda: aio_clac('math.tan('))
            abs_b.configure(command=lambda: aio_clac('abs('))
            fac_b.configure(command=lambda: aio_clac('math.factorial('))
            rad_b.configure(command=lambda: aio_clac('random.randint(')) # This will be tricky for user
            
            clear_b.configure(command=aio_clear)
            equal_b.configure(command=equalpress)
            entry.configure(textvariable=equation)
            
            one_at_a_time.configure(fg_color=("gray75", "gray25"))
            everything_at_once.configure(fg_color=("#3B8ED0", "#1F6AA5"))

    # text and buttons for sizes
    settings_text = CTkLabel(settings_root, text='Settings', font=("Arial", 16, "bold"))
    size_text = CTkLabel(settings_root, text='Size settings:', pady=5)
    size_small = CTkButton(settings_root, text='Small', command=small, width=btn_width)
    size_normal = CTkButton(settings_root, text='Medium', command=medium, width=btn_width)
    size_big = CTkButton(settings_root, text='Big', command=big, width=btn_width)
    # text and buttons for themes
    theme_text = CTkLabel(settings_root, text='Theme settings:', pady=5)
    theme_light = CTkButton(settings_root, text='Light', command=light_theme, width=btn_width)
    theme_dark = CTkButton(settings_root, text='Dark', command=dark_theme, width=btn_width)
    
    # calculation modes
    calculation_text = CTkLabel(settings_root, text='Calculation Mode:', pady=5)
    one_at_a_time = CTkButton(settings_root, text='One at a time', command=lambda: change_c('one'), width=btn_width)
    everything_at_once = CTkButton(settings_root, text='All at once', command=lambda: change_c('everything')
                                   , width=btn_width)

    # Initialize button states
    update_size_buttons('medium') # Default assumption
    update_theme_buttons(customtkinter.get_appearance_mode().lower())
    change_c(calc_mode)

    settings_text.grid(row=0, column=0, columnspan=3, pady=10)
    
    size_text.grid(row=1, column=0, columnspan=3)
    size_small.grid(row=2, column=0, padx=5, pady=5)
    size_normal.grid(row=2, column=1, padx=5, pady=5)
    size_big.grid(row=2, column=2, padx=5, pady=5)
    
    theme_text.grid(row=3, column=0, columnspan=3)
    theme_light.grid(row=4, column=0, padx=5, pady=5)
    theme_dark.grid(row=4, column=2, padx=5, pady=5)
    
    calculation_text.grid(row=5, column=0, columnspan=3)
    one_at_a_time.grid(row=6, column=0, padx=5, pady=5)
    everything_at_once.grid(row=6, column=2, padx=5, pady=5)


def get_width():
    return width // 8 -10

# frames
entry_frame = Frame(root, bg='white')
entry_frame.pack(fill=BOTH, expand=True)
button_frame = Frame(root, padx=0, bg='white')
button_frame.pack(fill=BOTH, expand=True)

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
b1.grid(row=1, column=1, sticky="nsew")
b2.grid(row=1, column=2, sticky="nsew")
b3.grid(row=1, column=3, sticky="nsew")
b4.grid(row=2, column=1, sticky="nsew")
b5.grid(row=2, column=2, sticky="nsew")
b6.grid(row=2, column=3, sticky="nsew")
b7.grid(row=3, column=1, sticky="nsew")
b8.grid(row=3, column=2, sticky="nsew")
b9.grid(row=3, column=3, sticky="nsew")
b0.grid(row=4, column=1, sticky="nsew")

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
equal_b.grid(row=4, column=2, sticky="nsew")
add_b.grid(row=1, column=4, sticky="nsew")
sub_b.grid(row=2, column=4, sticky="nsew")
mul_b.grid(row=3, column=4, sticky="nsew")
div_b.grid(row=4, column=4, sticky="nsew")
power_b.grid(row=0, column=4, sticky="nsew")
sqrt_b.grid(row=0, column=1, sticky="nsew")
exp_b.grid(row=0, column=0, sticky="nsew")
sin_b.grid(row=1, column=0, sticky="nsew")
cos_b.grid(row=2, column=0, sticky="nsew")
tan_b.grid(row=3, column=0, sticky="nsew")
abs_b.grid(row=0, column=3, sticky="nsew")
fac_b.grid(row=0, column=2, sticky="nsew")
rad_b.grid(row=4, column=0, sticky="nsew")
clear_b.grid(row=4, column=3, sticky="nsew")

# Configure grid weights
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)
button_frame.grid_columnconfigure(4, weight=1)
for i in range(5):
    button_frame.grid_rowconfigure(i, weight=1)

# creating & placing the calculations bar
total_exp_entry = Label(entry_frame, width=get_width()//2, text=total_exp, anchor=NE, padx=10, justify=CENTER, bg='white')
entry = Entry(entry_frame, borderwidth=2, width=get_width(), justify=CENTER, state='normal', bg='white')
total_exp_entry.pack(expand=True, fill=BOTH, anchor=N)
entry.pack(anchor=N, fill=X, padx=10, pady=(0, 10))

# shortcuts
root.bind('<Key-c>', button_clear)
root.bind('<Key-e>', lambda event: button_equal())
root.bind('<Escape>', lambda event: root.quit())
root.bind('<s>', lambda event: settings())
root.bind('<S>', lambda event: settings())

messagebox.showinfo('Tip', 'for the settings to pop up press s')
root.mainloop()
