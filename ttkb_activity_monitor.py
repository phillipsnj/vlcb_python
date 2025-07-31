from vlcb_server.network_threaded_client import VlcbClient

import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledText
from ttkbootstrap.constants import *


class DemoApp(tb.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        cbus_header = ':SB060N'
        self.stop_ouput = tb.BooleanVar()
        self.stop_ouput.set(False)

        self.scroll_cf = ScrolledText(self)
        self.scroll_cf.pack(side=BOTTOM, fill=X)

        self.scroll_cf.insert(END, 'first line')

        buttonbar = tb.Frame(self, style='primary.TFrame')
        buttonbar.pack(fill=X, pady=1, side=TOP)

        b1 = tb.Button(buttonbar, text='primary', bootstyle="primary", command=self.insert_rows)
        b1.pack(side=LEFT, padx=5, pady=5)

        self.b2 = tb.Button(buttonbar, text='Freeze', bootstyle=DANGER, command=self.toggle_scrolling)
        self.b2.pack(side=LEFT, padx=5, pady=5)

        b3 = tb.Button(buttonbar, text='Clear', bootstyle=SUCCESS, command=self.clear_text)
        b3.pack(side=LEFT, padx=5, pady=5)

        self.VLCB_client = VlcbClient(self.process_message, "localhost", 5550)
        #
        # self.VLCB_client.send(f'{cbus_header}0D;')
        #
        self.VLCB_client.start()

    def process_message(self, msg):
        if self.stop_ouput.get() == False:
            print(f'Message : {msg}')
            self.scroll_cf.insert(END, f'new message {msg}\n')
            self.scroll_cf.see(END)
        else:
            print("Don't insert message")

    def insert_rows(self):
            print('insert row')
            self.scroll_cf.insert(END, f'new line\n')
            self.scroll_cf.see(END)


    def clear_text(self):
        self.scroll_cf.delete(1.0, END)

    def toggle_scrolling(self):
        if self.stop_ouput.get() == True:
            self.stop_ouput.set(False)
            self.b2.config(text='Freeze', bootstyle=DANGER)
        else:
            self.stop_ouput.set(True)
            self.b2.config(text='Unfreeze', bootstyle=SUCCESS)


if __name__ == '__main__':
    app = tb.Window('MERG Demo APP')
    DemoApp(app)
    app.mainloop()