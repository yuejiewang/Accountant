from tkinter import *
from main import *

ws = Tk()
ws.geometry('400x300')
ws.title('Add Stuff')
ws['bg'] = '#5d8a82'
ws.attributes('-fullscreen', True)
font_default = ("Times bold", 14)

buyer_list = dict()
variable = StringVar()
variable.set("buyer")


def next_page():
    ws.destroy()
    check_out()


def add_buyer(choice):
    global buyer_list
    choice = variable.get()
    if choice == "all":
        for k in bill.keys():
            buyer_list[k] = 1
    else:
        buyer_list[choice] = 1
    # print(buyer_list)


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


lbl_content = StringVar()
lbl_content.set("Purchase: \n")
lbl = Label(
    textvariable=lbl_content,
    bg='#5d8a82'
    )
lbl.pack(fill=BOTH, expand=TRUE)


def loop_add():
    global buyer_list
    num_div = len(buyer_list)
    amount = e.get()
    e.delete(0, END)
    if amount[0] == '-':
        tot = add(num_div, list(buyer_list.keys()), -float(amount[1:]))
    else:
        tot = add(num_div, list(buyer_list.keys()), float(amount))
    buyer_list.clear()
    variable.set("buyer")
    tot_string = "Purchase: \n"
    for k in bill_string.keys():
        tot_string += k + " = " + bill_string[k] + " = %.2f\n" % bill_value[k]
    for k in bill.keys():
        tot_string += k + " = %.2f\n" % bill[k]
    tot_string += "total = %.2f\n" % tot
    lbl_content.set(tot_string)


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

ws.mainloop()
