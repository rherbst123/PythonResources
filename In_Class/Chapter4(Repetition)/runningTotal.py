total_shells = 0

for i in range(1,10):
    
    daily_shells = int(input(f"How many shells for day: {i}: "))
    total_shells += daily_shells

print(f"You have found {total_shells} shells")