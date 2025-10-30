deposit = "Deposit : 10000.0"
statement, amount = deposit.split(":")

print(statement, amount)

if statement.isalpha():
    print("input type is correct")
else:
    print("Error")

if amount.isdigit():
    print("input type is correct")
else:
    print("error")

