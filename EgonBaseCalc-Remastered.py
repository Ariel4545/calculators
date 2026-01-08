# imports
from tkinter import messagebox
from tkinter import *
import customtkinter
from customtkinter import *

# window
root = CTk()
width = 370
height = 560
screen_width = root.winfo_width()
screen_height = root.winfo_height()
placement_x = abs((screen_width // 2) - (width // 2))
placement_y = abs((screen_height // 2) - (height // 2))
root.geometry(f'{width}x{height}+{placement_x}+{placement_y}')
root.title('Egon Base calculator')
root.resizable(False, False)
root.configure(bg='white')
# logo = PhotoImage(file='Logo.png')
# root.iconphoto(False, logo)
operation_color = '#e0e0e0'
base = ['decimal']
set_appearance_mode('light')
total_exp = ''
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
        # if base == 'decimal':
        if operation == '+':
            entry.insert(0, f_num + s_num)
        if operation == '*':
            entry.insert(0, f_num * s_num)
        if operation == '/':
            try:
                entry.insert(0, f_num / s_num)
            except ZeroDivisionError:
                messagebox.showerror('Error', 'Divided by zero')
        if operation == '-':
            entry.insert(0, f_num - s_num)
    except ValueError:
        pass
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
    total_exp = f'{f_num} {operation} '
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
    total_exp = f'{f_num} {operation} '
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
    total_exp = f'{f_num} {operation} '
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
    total_exp = f'{f_num} {operation} '
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
        entry.configure(width=get_entry_width())

    def small():
        global button_height, button_width
        global width, height
        button_height, button_width = 3, 6
        width, height = 270, 310 + 30
        size()
        update_size_buttons('small')

    def medium():
        global button_height, button_width
        global width, height
        button_height, button_width = 6, 9
        width, height = 370, 530 + 30
        size()
        update_size_buttons('medium')

    def big():
        global button_height, button_width
        global width, height
        button_height, button_width = 9, 12
        width, height = 470, 730 + 30
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
    
    # Initialize button states
    update_size_buttons('medium') # Default assumption
    update_theme_buttons(customtkinter.get_appearance_mode().lower())

    settings_text.grid(row=0, column=0, columnspan=3, pady=10)
    
    size_text.grid(row=1, column=0, columnspan=3)
    size_small.grid(row=2, column=0, padx=5, pady=5)
    size_normal.grid(row=2, column=1, padx=5, pady=5)
    size_big.grid(row=2, column=2, padx=5, pady=5)
    
    theme_text.grid(row=3, column=0, columnspan=3)
    theme_light.grid(row=4, column=0, padx=5, pady=5)
    theme_dark.grid(row=4, column=2, padx=5, pady=5)

    light_theme()
    medium()


def get_entry_width():
    return (width//8) - 10


# creating button frame
entry_frame = Frame(root, bg='white')
entry_frame.pack(fill=BOTH, expand=True)
button_frame = Frame(root, padx=0, bg='white')
button_frame.pack(fill=BOTH, expand=True)

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
b1.grid(row=1, column=1, sticky="nsew")
b2.grid(row=1, column=2, sticky="nsew")
b3.grid(row=1, column=3, sticky="nsew")

b4.grid(row=2, column=1, sticky="nsew")
b5.grid(row=2, column=2, sticky="nsew")
b6.grid(row=2, column=3, sticky="nsew")

b7.grid(row=3, column=1, sticky="nsew")
b8.grid(row=3, column=2, sticky="nsew")
b9.grid(row=3, column=3, sticky="nsew")

b0.grid(row=4, column=3, sticky="nsew")

bA.grid(row=1, column=0, sticky="nsew")
bB.grid(row=2, column=0, sticky="nsew")
bC.grid(row=3, column=0, sticky="nsew")
bD.grid(row=4, column=0, sticky="nsew")
bE.grid(row=4, column=1, sticky="nsew")
bF.grid(row=4, column=2, sticky="nsew")

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
add_b.grid(row=1, column=4, sticky="nsew")
sub_b.grid(row=2, column=4, sticky="nsew")
mul_b.grid(row=3, column=4, sticky="nsew")
div_b.grid(row=4, column=4, sticky="nsew")
clear_b.grid(row=5, column=4, sticky="nsew")
decimal_button.grid(row=5, column=0, sticky="nsew")
binary_button.grid(row=5, column=1, sticky="nsew")
octal_button.grid(row=5, column=2, sticky="nsew")
hexadecimal_button.grid(row=5, column=3, sticky="nsew")

# Configure grid weights
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)
button_frame.grid_columnconfigure(4, weight=1)
for i in range(6):
    button_frame.grid_rowconfigure(i, weight=1)

# creating & placing the calculations bar
total_exp_entry = Label(entry_frame, width=get_entry_width()//2, text=total_exp, anchor=NE, padx=10, justify=CENTER, bg='white')
entry = Entry(entry_frame, borderwidth=2, width=get_entry_width(), justify=CENTER, state='normal', bg='white')
total_exp_entry.pack(expand=True, fill=BOTH, anchor=N)
entry.pack(anchor=N, fill=X, padx=10, pady=(0, 10))

# shortcuts
root.bind('<c>', button_clear)
root.bind('<e>', lambda event: button_equal())
root.bind('<Escape>', lambda event: root.quit())
root.bind('<s>', settings)

if __name__ == '__main__':
    base_settings()
    messagebox.showinfo('Tip', 'for the settings to pop up press s')

root.mainloop()
