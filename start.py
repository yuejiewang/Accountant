from tkinter import *
from main import *

ws = Tk()
ws.geometry('400x300')
ws.title('Start Page')
ws['bg'] = '#5d8a82'
font_default = ("Times bold", 14)


def next_page():
    ws.destroy()
    if len(bill) == 0:
        exit()
    import add_stuff


e = Entry(
    ws,
    font=font_default,
    )
e.pack(pady=10, side=TOP)


def print_participants():
    ret = "Participants: \n"
    for k in bill.keys():
        ret += "%s\n" % k
    return ret


lbl_content = StringVar()
lbl_content.set("Participants: \n")
lbl = Label(
    textvariable=lbl_content,
    bg='#5d8a82'
    )
lbl.pack(fill=BOTH, expand=TRUE)


def add_participant():
    global lbl_content
    name = e.get()
    if name == "":
        return
    e.delete(0, END)
    if name not in bill.keys():
        bill[name] = 0
        lbl_content.set(print_participants())


def enter(event):
    add_participant()


def proceed(event):
    next_page()


Button(
    ws,
    text="Proceed to add items",
    font=font_default,
    command=next_page
    ).pack(fill=X, side=BOTTOM)
Button(
    ws,
    text="Add participant",
    font=font_default,
    command=add_participant
    ).pack(fill=X, side=BOTTOM)

ws.bind('<Return>', enter)
ws.bind('<Shift-Return>', proceed)
ws.mainloop()
