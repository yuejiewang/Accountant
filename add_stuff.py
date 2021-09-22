from tkinter import *
from main import *

ws = Tk()
ws.geometry('400x300')
ws.title('Add Stuff')
ws['bg'] = '#5d8a82'
ws.attributes('-fullscreen', True)
font_default = ("Times bold", 14)

buyer_list = list()
variable = StringVar()
variable.set("buyer")
buy_content = StringVar()
buy_content.set("By: \n")


def next_page():
    ws.destroy()
    check_out()


def add_buyer(choice):
    global buyer_list
    choice = variable.get()
    if choice == "all":
        buyer_list = list(bill.keys())
    else:
        if choice in buyer_list:
            buyer_list.remove(choice)
        else:
            buyer_list.append(choice)
    c = "By: "
    for b in buyer_list:
        c += "%s " % b
    buy_content.set(c + "\n")


opts = list(bill.keys())
opts.append("all")
menu = OptionMenu(
    ws,
    variable,
    *opts,
    command=add_buyer
    )
menu.pack(pady=10, side=TOP)


e = Entry(
    ws,
    font=font_default,
    )
e.pack(pady=10, side=TOP)


buy_lbl = Label(
    textvariable=buy_content,
    bg='#5d8a82'
    )
buy_lbl.pack(pady=10, side=TOP)


lbl_content = StringVar()
lbl_content.set("Purchase: \n")
lbl = Label(
    textvariable=lbl_content,
    bg='#5d8a82'
    )
lbl.pack(pady=10, side=TOP)


def loop_add():
    global buyer_list
    num_div = len(buyer_list)
    if num_div == 0:
        buy_content.set("No buyer, please enter at least one buyer.\n")
        return
    amount = e.get()
    e.delete(0, END)
    if amount == "":
        return
    if amount[0] == '-':
        tot = add(num_div, buyer_list, -float(amount[1:]))
    else:
        tot = add(num_div, buyer_list, float(amount))
    variable.set("buyer")
    tot_string = "Purchase: \n"
    for k in bill_string.keys():
        tot_string += k + " = " + bill_string[k] + " = %.2f\n" % bill_value[k]
    tot_string += "\nPersonal sum: \n"
    for k in bill.keys():
        tot_string += k + " = %.2f\n" % bill[k]
    tot_string += "\nTOTAL:\n%.2f\n" % tot
    lbl_content.set(tot_string)


def enter(event):
    loop_add()


def proceed(event):
    next_page()


Button(
    ws,
    text="Proceed to check-out",
    font=font_default,
    command=next_page
    ).pack(fill=X, side=BOTTOM)
Button(
    ws,
    text="Add item",
    font=font_default,
    command=loop_add
    ).pack(fill=X, side=BOTTOM)

ws.bind('<Return>', enter)
ws.bind('<Shift-Return>', proceed)
ws.mainloop()
