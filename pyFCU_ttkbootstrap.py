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
        self.rowconfigure(1, weight=10)
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
        ttk.Label(self, text='Main Menu', bootstyle='inverse-primary').pack(expand=True, fill='both')
        # self.place(relx = 0, rely = 0, relwidth = 1, relheight = 0.1)
        self.grid(row=0, column=0, sticky='nsew', columnspan=2)


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        print(f'Test Main')
        ttk.Label(self, text='Cbus Nodes', bootstyle='inverse-secondary').pack(expand=True, fill='both')
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
