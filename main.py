bill = dict()
bill_string = dict()
bill_value = dict()
total = 0


def add(num_div, list_names, amount):
    global total, bill_string, bill_value
    total += amount
    list_names.sort()
    div_amount = amount / num_div
    for i in range(num_div):
        bill[list_names[i]] += div_amount
    key_string = list_names[0]
    for i in range(num_div-1):
        key_string += "::" + list_names[i+1]
    if key_string in bill_string.keys():
        bill_string[key_string] += " + %.2f" % amount
        bill_value[key_string] += amount
    else:
        bill_string[key_string] = "%.2f" % amount
        bill_value[key_string] = amount
    return total


def check_out():
    global total, bill_string, bill_value
    '''
    for k in bill_string.keys():
        bill_string[k] = k + " = " + bill_string[k] + " = %.2f" % bill_value[k]
        print(bill_string[k])
    '''
    for k in bill.keys():
        bill[k] = k + " = %.2f" % bill[k]
        print(bill[k])
    tot_string = "total = %.2f" % total
    print("total = %.2f" % total)
    return tot_string


if __name__ == '__main__':
    import start
