import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class TtkFcu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        print('Test Running')
        # self.title(title)
        # self.geometry(f'{size[0]}x{size[1]}')
        # self.minsize(*size)
        self.pack(fill="both", expand=YES)
        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        # self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=7)
        self.rowconfigure(2, weight=5)
        # self.rowconfigure(2, weight=1)
        # self.colors = self.style.colors
        self.menu = Menu(self)
        self.main = Main(self)
        self.event = Event(self)
        self.send_messages = SentMessages(self)
        self.received_messages = RecievedMessages(self)
        self.footer = Footer(self)


class Menu(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        print(f'Test Menu')
        # ttk.Label(self, text='Main Menu', bootstyle='inverse-primary').pack()
        # self.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)
        main_menu = ttk.Menu(self)
        # file_menu = tk.Menu(main_menu, tearoff=False)
        # file_menu.add_command(label='Add', command=self.do_something)
        # file_menu.add_command(label='Exit', command=parent.destroy)
        # parent.config(menu=main_menu)
        self.variable = tk.StringVar()
        ttk.Menubutton(self, text='File', menu=main_menu).pack(side='left')
        main_menu.add_radiobutton(label='Open', variable=self, value='Open')
        main_menu.add_radiobutton(label='Save', variable=self, value='Save')
        main_menu.add_radiobutton(label='Save As', variable=self, value='Save As')
        main_menu.add_separator()
        self.grid(row=0, column=0, sticky='nsew', columnspan=2)

    def do_something(self):
        print('Do something')


class Main(ttk.Labelframe):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(text='Modules ', bootstyle=SECONDARY)
        print(f'Test Main')
        ttk.Label(self, text='Modules', bootstyle='inverse-secondary').pack(expand=True, fill='both')
        # self.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.8)
        self.grid(row=1, column=0, sticky='nsew')


class Event(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text='Cbus Node Events', bootstyle='inverse-info').pack(expand=True, fill='both')
        # self.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.8)
        self.grid(row=2, column=0, sticky='nsew')


class SentMessages(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text='Sent Messages', bootstyle='inverse-danger').pack(expand=True, fill='both')
        # self.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.8)
        self.grid(row=2, column=1, sticky='nsew')


class RecievedMessages(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text='Recieved Messages', bootstyle='inverse-warning').pack(expand=True, fill='both')
        # self.place(relx = 0, rely = 0.1, relwidth = 1, relheight = 0.8)
        self.grid(row=1, column=1, sticky='nsew')


class Footer(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self, text='Bottom Bar', bootstyle='inverse-dark').pack(expand=True, fill='both')
        # self.place(relx = 0, relwidth = 1, rely = 0.9, relheight = 0.1)
        self.grid(row=3, column=0, sticky='nsew', columnspan=2)


if __name__ == '__main__':
    app = ttk.Window("TTKBootstrap FCU Demo")
    size = (800, 600)
    app.geometry(f'{size[0]}x{size[1]}')
    app.minsize(*size)
    TtkFcu(app)
    app.mainloop()
