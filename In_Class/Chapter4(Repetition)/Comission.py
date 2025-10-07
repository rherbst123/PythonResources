keep_going = input("Y or N: ")

sales = 0
commission_rate = 0

while keep_going == "Y":
    if keep_going == "Y":
        sales = int(input("Enter the sales: "))
        commission_rate = int(input("Enter the commission: "))

        commission = sales * commission_rate

        print(commission)
        keep_going = input("Another one: ")
    elif keep_going == "N":
        break




