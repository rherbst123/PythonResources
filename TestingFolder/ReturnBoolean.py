def give_boolean(a,b):
    name = input("ENter your name")
    result = a > b
    return result, name

def main():
    result, name = give_boolean(10,5)

    print(result, name)
main()