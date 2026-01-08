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
calc_mode = 'one'
operation = None
f_num = 0

def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear(event=None):
    entry.delete(0, END)


def button_equal(event=None):
    global total_exp
    if operation is None:
        return
    second_number = entry.get()
    total_exp += second_number
    entry.delete(0, END)
    try:
        s_num = int(second_number)
    except ValueError:
        return
    
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
    total_exp = ''

def button_add():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    try:
        f_num = int(first_number)
    except ValueError:
        f_num = 0
    operation = '+'
    total_exp = f'{f_num} {operation}'
    entry.delete(0, END)


def button_sub():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    try:
        f_num = int(first_number)
    except ValueError:
        f_num = 0
    operation = '-'
    total_exp = f'{f_num} {operation}'
    entry.delete(0, END)


def button_mul():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    try:
        f_num = int(first_number)
    except ValueError:
        f_num = 0
    operation = '*'
    total_exp = f'{f_num} {operation}'
    entry.delete(0, END)


def button_div():
    first_number = entry.get()
    global f_num
    global operation
    global total_exp
    try:
        f_num = int(first_number)
    except ValueError:
        f_num = 0
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
    settings_root.title('Settings')
    settings_root.geometry('400x300')
    settings_text = CTkLabel(settings_root, text='Settings', font=("Arial", 16, "bold"))
    btn_width = 80

    def size():
        global padx_b, pady_b
        for i in f_list:
            i.configure(padx=padx_b, pady=pady_b)
        root.geometry(f'{width}x{height}')
        entry.configure(width=get_entry_width())

    def small():
        global padx_b, pady_b
        global width, height
        padx_b, pady_b = 1, 3
        width, height = 320, 430 + 30
        size()
        update_size_buttons('small')

    def medium():
        global padx_b, pady_b
        global width, height
        padx_b, pady_b = 2, 6
        width, height = 355, 455 + 30
        size()
        update_size_buttons('medium')

    def big():
        global padx_b, pady_b
        global width, height
        padx_b, pady_b = 4, 12
        width, height = 370, 500 + 30
        size()
        update_size_buttons('big')

    def update_size_buttons(active_size):
        # Visual feedback for size buttons
        buttons = {'small': size_small, 'medium': size_normal, 'big': size_big}
        for name, btn in buttons.items():
            if name == active_size:
                btn.configure(fg_color=("#3B8ED0", "#1F6AA5")) # Active color
            else:
                btn.configure(fg_color=("gray75", "gray25")) # Inactive color

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
            i.configure(bg=btn_num_bg, foreground=text_color)
        for i in b_list:
            i.configure(bg=btn_op_bg, fg=text_color)
        equal_b.configure(bg='#005f73', fg='white') # Teal for equal
        entry.configure(bg='#2b2b2b', foreground='white', insertbackground='white')
        total_exp_entry.configure(bg=bg_color, foreground='gray')
        
        customtkinter.set_appearance_mode('dark')
        update_theme_buttons('dark')

    def light_theme():
        # Light Theme Colors
        bg_color = 'white'
        
        root.configure(bg=bg_color)
        entry_frame.configure(bg=bg_color)
        button_frame.configure(bg=bg_color)
        
        for i in n_list:
            i.configure(bg='SystemButtonFace', foreground='black')
        for i in b_list:
            i.configure(bg=operation_color, foreground='black')
        equal_b.configure(bg=equal_color, fg='black')
        entry.configure(bg='white', foreground='black', insertbackground='black')
        total_exp_entry.configure(bg='white', foreground='gray')
        
        customtkinter.set_appearance_mode('light')
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
            for i in range(len(n_list)):
                n_list[i].configure(command=lambda i=i: button_click(i))
            div_b.configure(command=button_div), mul_b.configure(command=button_mul),\
            add_b.configure(command=button_add), sub_b.configure(command=button_sub),\
            clear_b.configure(command=button_clear)
            equal_b.configure(command=button_equal)
            entry.configure(textvariable=None)
            
            one_at_a_time.configure(fg_color=("#3B8ED0", "#1F6AA5"))
            everything_at_once.configure(fg_color=("gray75", "gray25"))
        else:
            for i, button in enumerate(n_list):
                button.configure(command=lambda i=i: aio_clac(i))
            div_b.configure(command=lambda: aio_clac('/')), mul_b.configure(command=lambda: aio_clac('*'))\
                , add_b.configure(command=lambda: aio_clac('+')), sub_b.configure(command=lambda: aio_clac('-'))\
                , clear_b.configure(command=aio_clear)
            equal_b.configure(command=equalpress)
            entry.configure(textvariable=equation)
            
            one_at_a_time.configure(fg_color=("gray75", "gray25"))
            everything_at_once.configure(fg_color=("#3B8ED0", "#1F6AA5"))

    # text and buttons for sizes
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
    update_size_buttons('small') # Default assumption, logic could be improved to track actual size
    update_theme_buttons(customtkinter.get_appearance_mode().lower())
    change_c(calc_mode) # Set initial state visual

    # placing
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


def get_entry_width():
    return (width // 8) - 10


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
b1.grid(row=1, column=0, sticky="nsew")
b2.grid(row=1, column=1, sticky="nsew")
b3.grid(row=1, column=2, sticky="nsew")

b4.grid(row=2, column=0, sticky="nsew")
b5.grid(row=2, column=1, sticky="nsew")
b6.grid(row=2, column=2, sticky="nsew")

b7.grid(row=3, column=0, sticky="nsew")
b8.grid(row=3, column=1, sticky="nsew")
b9.grid(row=3, column=2, sticky="nsew")

b0.grid(row=4, column=0, sticky="nsew")

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
equal_b.grid(row=4, column=1, sticky="nsew")
add_b.grid(row=1, column=4, sticky="nsew")
sub_b.grid(row=2, column=4, sticky="nsew")
mul_b.grid(row=3, column=4, sticky="nsew")
div_b.grid(row=4, column=4, sticky="nsew")
clear_b.grid(row=4, column=2, sticky="nsew")

# Configure grid weights to fill space
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(4, weight=1)
for i in range(1, 5):
    button_frame.grid_rowconfigure(i, weight=1)

# creating & placing the calculations bar
total_exp_entry = Label(entry_frame, width=get_entry_width()//2, text=total_exp, anchor=NE, padx=10, justify=CENTER, bg='white')
entry = Entry(entry_frame, borderwidth=2, width=get_entry_width(), justify=CENTER, state='normal', bg='white')
total_exp_entry.pack(expand=True, fill=BOTH, anchor=N)
entry.pack(anchor=N, fill=X, padx=10, pady=(0, 10))

# shortcuts
root.bind('<Key-c>', button_clear)
root.bind('<Key-e>', lambda event: button_equal())
# root.bind('<1>', lambda event: button_click(1))
root.bind('<Escape>', lambda event: root.quit())
root.bind('<Key-s>', lambda event: settings())
root.bind('<Key-S>', lambda event: settings())

tkinter.messagebox.showinfo('Tip', 'for the settings to pop up press s')
root.mainloop()
