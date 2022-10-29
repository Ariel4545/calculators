# imports
import tkinter.messagebox
from tkinter import *

# window
root = Tk()
width = 340
height = 430
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
try:
    logo = PhotoImage(file='Logo.png')
    root.iconphoto(False, logo)
except BaseException:
    pass


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear(event=None):
    entry.delete(0, END)


def button_equal(event=None):
    second_number = entry.get()
    entry.delete(0, END)
    s_num = int(second_number)
    if operation == '+':
        entry.insert(0, f_num + s_num)
    if operation == '*':
        entry.insert(0, f_num * s_num)
    if operation == '/':
        entry.insert(0, f_num / s_num)
    if operation == '-':
        entry.insert(0, f_num - s_num)


def button_add():
    first_number = entry.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = '+'
    entry.delete(0, END)


def button_sub():
    first_number = entry.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = '-'
    entry.delete(0, END)


def button_mul():
    first_number = entry.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = '*'
    entry.delete(0, END)


def button_div():
    first_number = entry.get()
    global f_num
    global operation
    f_num = int(first_number)
    operation = '/'
    entry.delete(0, END)


def settings(event=None):
    # window
    settings_root = Toplevel()
    settings_root.resizable()
    settings_text = Label(settings_root, text='Settings', font='arial 14 bold')
    settings_text.grid(row=0)
    # text and buttons for sizes
    size_text = Label(settings_root, text='Size settings:',font='arial 10 underline', pady=5)
    size_small = Button(settings_root, text='Small')
    size_normal = Button(settings_root, text='Medium')
    size_big = Button(settings_root, text='Big')
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
        global padx_b,  pady_b
        for i in f_list:
            i.config(padx=padx_b, pady=pady_b)
        root.geometry(f'{width}x{height}')

    def small():
        global padx_b,  pady_b
        global width, height
        padx_b, pady_b = 1, 3
        size_small.config(bg='grey'), size_normal.config(bg='white'), size_big.config(bg='white')
        width, height = 340, 430
        size()

    def medium():
        global padx_b,  pady_b
        global width, height
        padx_b, pady_b = 2, 6
        width, height = 355, 455
        size_small.config(bg='white'), size_normal.config(bg='grey'), size_big.config(bg='white')
        size()

    def big():
        global padx_b,  pady_b
        global width, height
        padx_b, pady_b = 4, 12
        width, height = 370, 500
        size_small.config(bg='white'), size_normal.config(bg='white'), size_big.config(bg='grey')
        size()

    size_small.config(command=small), size_normal.config(command=medium), size_big.config(command=big)
    small()

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


button_frame = Frame(root, padx=20)
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

n_list = [b0, b1, b2, b3, b4, b4, b5, b6, b7, b8, b9]

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
entry = Entry(root, borderwidth=2, width=40, justify=CENTER, state='normal')
entry.grid(row=0, column=0, columnspan=4, sticky=N)

# shortcuts
root.bind('<Key-c>', button_clear)
root.bind('<Key-e>', lambda event: button_equal())
# root.bind('<1>', lambda event: button_click(1))
root.bind('<Escape>', lambda event: root.quit())
root.bind('<Key-s>', settings)

tkinter.messagebox.showinfo('Tip', 'for the settings to pop up press s')
root.mainloop()

