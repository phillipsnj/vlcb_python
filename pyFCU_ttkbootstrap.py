import ttkbootstrap as ttk
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.constants import *

app = ttk.Window()
colors = app.style.colors

coldata = [
    {"text": "LicenseNumber", "stretch": False},
    "CompanyName",
    {"text": "UserCount", "stretch": False},
]

rowdata = [
    ('A123', 'IzzyCo', 12),
    ('A136', 'Kimdee Inc.', 45),
    ('A158', 'Farmadding Co.', 36)
]


def select_node(_):
    nodes = dt.get_rows(selected=True)
    for node in nodes:
        print(f'Selected: {node.values}')


dt = Tableview(
    master=app,
    coldata=coldata,
    rowdata=rowdata,
    paginated=True,
    searchable=True,
    bootstyle=PRIMARY,
    stripecolor=(colors.light, None),
)
dt.bind_all("<<TreeviewSelect>>", select_node)
dt.pack(fill=BOTH, expand=YES, padx=10, pady=10)

print('Test Running')
app.mainloop()
