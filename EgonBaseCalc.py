# imports
from tkinter import messagebox
from tkinter import *

# window
root = Tk()
width = 370
height = 530
screen_width = root.winfo_width()
screen_height = root.winfo_height()
placement_x = abs((screen_width // 2) - (width // 2))
placement_y = abs((screen_height // 2) - (height // 2))
root.geometry(f'{width}x{height}+{placement_x}+{placement_y}')
root.title('Egon Base calculator')
root.resizable(False, False)
root.configure(bg='white')
logo = PhotoImage(file='Logo.png')
root.iconphoto(False, logo)
operation_color = '#e0e0e0'
base = ['decimal']


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
    # if base == 'decimal':
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
    global last_base, base
    root.title(f'Egon Base calculator - {mode}')
    last_base = base[-1]
    base.append(mode)

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
        convert(last_base, 'decimal')

    elif mode == 'binary':
        b1.configure(state='normal')
        b2.configure(state='disabled')
        b3.configure(state='disabled')
        b4.configure(state='disabled')
        b5.configure(state='disabled')
        b6.configure(state='disabled')
        b7.configure(state='disabled')
        b8.configure(state='disabled')
        b9.configure(state='disabled')
        b0.configure(state='normal')
        bA.configure(state='disabled')
        bB.configure(state='disabled')
        bC.configure(state='disabled')
        bD.configure(state='disabled')
        bE.configure(state='disabled')
        bF.configure(state='disabled')
        equal_b.configure(state='disabled')
        add_b.configure(state='disabled')
        sub_b.configure(state='disabled')
        mul_b.configure(state='disabled')
        div_b.configure(state='disabled')
        convert(last_base, 'binary')

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
        equal_b.configure(state='disabled')
        add_b.configure(state='disabled')
        sub_b.configure(state='disabled')
        mul_b.configure(state='disabled')
        div_b.configure(state='disabled')
        convert(last_base, 'octal')

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
        equal_b.configure(state='disabled')
        add_b.configure(state='disabled')
        sub_b.configure(state='disabled')
        mul_b.configure(state='disabled')
        div_b.configure(state='disabled')
        convert(last_base, 'hexadecimal')


def convert(fromBase, toBase):
    if not entry.get() == '':
        num = entry.get()
        entry.delete(0, END)
        str(fromBase)
        if fromBase == 'decimal':
            if toBase == 'binary':
                num = (bin(int(num)))[2:]
            elif toBase == 'octal':
                num = (oct(int(num)))[2:]
            elif toBase == 'hexadecimal':
                num = (hex(int(num)))[2:]
        elif fromBase == 'binary':
            if toBase == 'decimal':
                num = int(num, 2)
            elif toBase == 'octal':
                num = oct(int(num, 2))[2:]
            elif toBase == 'hexadecimal':
                num = hex(int(num, 2))[2:]
        elif fromBase == 'octal':
            if toBase == 'decimal':
                num = int(num, 8)
            elif toBase == 'binary':
                num = bin(int(num, 8))[2:]
            elif toBase == 'hexadecimal':
                num = hex(int(num, 8))[2:]
        else:
            if toBase == 'decimal':
                num = int(num, 16)
            elif toBase == 'binary':
                num = bin(int(num, 16))[2:]
            elif toBase == 'octal':
                num = oct(int(num, 16))[2:]
        entry.insert(0, (num))


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
        for i in b_list:
            i.config(width=button_width, height=button_height)
        root.geometry(f'{width}x{height}')

    def small():
        global button_height, button_width
        global width, height
        button_height, button_width = 3, 6
        size_small.config(bg='grey'), size_normal.config(bg='white'), size_big.config(bg='white')
        width, height = 270, 310
        size()

    def medium():
        global button_height, button_width
        global width, height
        button_height, button_width = 6, 9
        width, height = 370, 530
        size_small.config(bg='white'), size_normal.config(bg='grey'), size_big.config(bg='white')
        size()

    def big():
        global button_height, button_width
        global width, height
        button_height, button_width = 9, 12
        width, height = 470, 730
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
        entry.config(bg='#373737', foreground='green')

    def light_theme():
        theme_dark.config(bg='white'), theme_light.config(bg='grey')
        for i in n_list:
            i.config(bg='SystemButtonFace')
        for i in b_list:
            i.config(bg=operation_color)
        entry.config(bg='white', foreground='black')

    theme_dark.config(command=dark_theme), theme_light.config(command=light_theme)
    light_theme()


# creating button frame
button_frame = Frame(root, )
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

bA = Button(button_frame, text="A", command=lambda: button_click("A"), relief=FLAT, padx=padx_b, pady=pady_b,
            height=button_height
            , width=button_width)
bB = Button(button_frame, text="B", command=lambda: button_click("B"), relief=FLAT, padx=padx_b, pady=pady_b,
            height=button_height
            , width=button_width)
bC = Button(button_frame, text="C", command=lambda: button_click("C"), relief=FLAT, padx=padx_b, pady=pady_b,
            height=button_height
            , width=button_width)
bD = Button(button_frame, text="D", command=lambda: button_click("D"), relief=FLAT, padx=padx_b, pady=pady_b,
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

b0.grid(row=4, column=3)

bA.grid(row=1, column=0)
bB.grid(row=2, column=0)
bC.grid(row=3, column=0)
bD.grid(row=4, column=0)
bE.grid(row=4, column=1)
bF.grid(row=4, column=2)

# creating operations buttons
padx_oper = padx_b
pady_oper = pady_b
equal_b = Button(button_frame, text="=", padx=padx_oper, pady=pady_oper, command=lambda: button_equal(), relief=FLAT,
                 height=button_height
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
decimal_button = Button(button_frame, text="DEC", command=lambda: base_settings(),
                        relief=FLAT, padx=padx_b, pady=pady_b,
                        height=button_height, bg=operation_color
                        , width=button_width)
binary_button = Button(button_frame, text="BIN", padx=padx_oper, pady=pady_oper, command=lambda: base_settings(
    'binary'),
                       relief=FLAT,
                       height=button_height, bg=operation_color
                       , width=button_width)
octal_button = Button(button_frame, text="OCT", padx=padx_oper, pady=pady_oper, command=lambda: base_settings(
    'octal'),
                      relief=FLAT,
                      height=button_height, bg=operation_color
                      , width=button_width)
hexadecimal_button = Button(button_frame, text="HEX", padx=padx_oper, pady=pady_oper, command=lambda: base_settings(
    'hexadecimal'),
                            relief=FLAT,
                            height=button_height, bg=operation_color
                            , width=button_width)

n_list = [b1, b2, b3, b4, b5, b5, b6, b7, b8, b9, b0, bA, bB, bC, bD, bE, bF]
b_list = [equal_b, add_b, sub_b, mul_b, div_b, decimal_button, binary_button, octal_button, hexadecimal_button, clear_b]
f_list = n_list + b_list
# placing operations buttons
add_b.grid(row=1, column=4)
sub_b.grid(row=2, column=4)
mul_b.grid(row=3, column=4)
div_b.grid(row=4, column=4)
clear_b.grid(row=5, column=4)
decimal_button.grid(row=5, column=0)
binary_button.grid(row=5, column=1)
octal_button.grid(row=5, column=2)
hexadecimal_button.grid(row=5, column=3)

# creating & placing the calculations bar
entry = Entry(root, borderwidth=2, width=40, justify=CENTER, state='normal')
entry.grid(row=0, column=0, columnspan=4, sticky=N)

# shortcuts
root.bind('<c>', button_clear)
root.bind('<e>', lambda event: button_equal())
root.bind('<Escape>', lambda event: root.quit())
root.bind('<s>', settings)

if __name__ == '__main__':
    base_settings()
    messagebox.showinfo('Tip', 'for the settings to pop up press s')

root.mainloop()
