# imports
from tkinter import *

# window
root = Tk()
width = 400
height = 530
screen_width = root.winfo_width()
screen_height = root.winfo_height()
placement_x = abs((screen_width // 2) - (width // 2))
placement_y = abs((screen_height // 2) - (height // 2))
root.geometry(f'{width}x{height}+{placement_x}+{placement_y}')
root.title('Egon Base calculator')
root.resizable(False, False)
root.configure(bg='white')


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


def base_settings(mode='decimal'):
    root.title(f'Egon Base calculator - {mode}')
    if not entry.get() == '':
        # convert.method
        print('converted!')


    if mode == 'decimal':
        b1.configure(state='normal')
        b2.configure(state='normal')
        b3.configure(state='normal')
        b4.configure(state='normal')
        b5.configure(state='normal')
        b6.configure(state='normal')
        b7.configure(state='normal')
        b8.configure(state='normal')
        b9.configure(state='normal')
        b0.configure(state='normal')
        bA.configure(state='disabled')
        bB.configure(state='disabled')
        bC.configure(state='disabled')
        bD.configure(state='disabled')
        bE.configure(state='disabled')
        bF.configure(state='disabled')


    elif mode == 'binary':
        b1.configure(state='normal')
        b2.configure(state='normal')
        b3.configure(state='disabled')
        b4.configure(state='disabled')
        b5.configure(state='disabled')
        b6.configure(state='disabled')
        b7.configure(state='disabled')
        b8.configure(state='disabled')
        b9.configure(state='disabled')
        b0.configure(state='disabled')
        bA.configure(state='disabled')
        bB.configure(state='disabled')
        bC.configure(state='disabled')
        bD.configure(state='disabled')
        bE.configure(state='disabled')
        bF.configure(state='disabled')


    elif mode == 'octal':
        b1.configure(state='normal')
        b2.configure(state='normal')
        b3.configure(state='normal')
        b4.configure(state='normal')
        b5.configure(state='normal')
        b6.configure(state='normal')
        b7.configure(state='normal')
        b8.configure(state='disabled')
        b9.configure(state='disabled')
        b0.configure(state='normal')
        bA.configure(state='disabled')
        bB.configure(state='disabled')
        bC.configure(state='disabled')
        bD.configure(state='disabled')
        bE.configure(state='disabled')
        bF.configure(state='disabled')

    elif mode == 'hexadecimal':
        b1.configure(state='normal')
        b2.configure(state='normal')
        b3.configure(state='normal')
        b4.configure(state='normal')
        b5.configure(state='normal')
        b6.configure(state='normal')
        b7.configure(state='normal')
        b8.configure(state='normal')
        b9.configure(state='normal')
        b0.configure(state='normal')
        bA.configure(state='normal')
        bB.configure(state='normal')
        bC.configure(state='normal')
        bD.configure(state='normal')
        bE.configure(state='normal')
        bF.configure(state='normal')


# def convert(base):
#     num = entry.get()
#     if base == 'binary':
#         
button_frame = Frame(root, padx=20)
button_frame.grid(row=1)
# creating numerical buttons
padx_b = 2
pady_b = 2
button_height = 6
button_width = 9
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

bA = Button(button_frame, text="A", command=lambda: button_click("A"), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
bB = Button(button_frame, text="B", command=lambda: button_click("B"), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
bC = Button(button_frame, text="C", command=lambda: button_click("C"), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
bD = Button(button_frame, text="D", command=lambda: button_click("D"), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
bE = Button(button_frame, text="E", command=lambda: button_click("E"), padx=padx_b, pady=pady_b, relief=FLAT,
            height=button_height
            , width=button_width)
bF = Button(button_frame, text="F", command=lambda: button_click("F"), padx=padx_b, pady=pady_b, relief=FLAT,
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

bA.grid(row=1, column=0)
bB.grid(row=2, column=0)
bC.grid(row=3, column=0)
bD.grid(row=4, column=0)
bE.grid(row=5, column=0)
bF.grid(row=6, column=0)

# creating operations buttons
padx_oper = padx_b
pady_oper = pady_b
equal_b = Button(button_frame, text="=", padx=padx_oper, pady=pady_oper, command=lambda: button_equal(), relief=FLAT,
                 height=button_height
                 , width=button_width)
add_b = Button(button_frame, text="+", padx=padx_oper, pady=pady_oper, command=lambda: button_add(), relief=FLAT,
               height=button_height
               , width=button_width)
sub_b = Button(button_frame, text="-", padx=padx_oper, pady=pady_oper, command=lambda: button_sub(), relief=FLAT,
               height=button_height
               , width=button_width)
mul_b = Button(button_frame, text="*", padx=padx_oper, pady=pady_oper, command=lambda: button_mul(), relief=FLAT,
               height=button_height
               , width=button_width)
div_b = Button(button_frame, text="/", padx=padx_oper, pady=pady_oper, command=lambda: button_div(), relief=FLAT,
               height=button_height
               , width=button_width)
clear_b = Button(button_frame, text="X", padx=padx_oper, pady=pady_oper, command=lambda: button_clear(), relief=FLAT,
                 height=button_height
                 , width=button_width)
decimal_button = Button(button_frame, text="DEC", padx=padx_oper, pady=pady_oper, command=lambda: base_settings(),
                        relief=FLAT,
                        height=button_height
                        , width=button_width)
binary_button = Button(button_frame, text="BIN", padx=padx_oper, pady=pady_oper, command=lambda: base_settings(
    'binary'),
                       relief=FLAT,
                       height=button_height
                       , width=button_width)
octal_button = Button(button_frame, text="OCT", padx=padx_oper, pady=pady_oper, command=lambda: base_settings(
    'octal'),
                      relief=FLAT,
                      height=button_height
                      , width=button_width)
hexadecimal_button = Button(button_frame, text="HEX", padx=padx_oper, pady=pady_oper, command=lambda: base_settings(
    'hexadecimal'),
                            relief=FLAT,
                            height=button_height
                            , width=button_width)

# placing operations buttons
equal_b.grid(row=4, column=2)
add_b.grid(row=1, column=4)
sub_b.grid(row=2, column=4)
mul_b.grid(row=3, column=4)
div_b.grid(row=4, column=4)
clear_b.grid(row=4, column=3)
decimal_button.grid(row=5, column=1)
binary_button.grid(row=5, column=2)
octal_button.grid(row=5, column=3)
hexadecimal_button.grid(row=5, column=4)

# creating & placing the calculations bar
entry = Entry(root, borderwidth=2, width=40, justify=CENTER, state='normal')
entry.grid(row=0, column=0, columnspan=4, sticky=N)

# shortcuts
root.bind('<c>', button_clear)

base_settings()
root.mainloop()
