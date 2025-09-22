def change_name(arg):
    print("I am changing")
    arg = 0
    print("now the value is", arg)

def main():
    value = 99
    print("Value", value)
    change_name(value)
    print("In main the value is: ", value)

main()