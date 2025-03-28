# 10. Tuition Increase
#  At one college, the tuition for a full-time student is $8,000 per semester. It has been announced 
# that the tuition will increase by 3 percent each year for the next 5 years. Write a program 
# with a loop that displays the projected semester tuition amount for the next 5 years.

tuition = 8000
rate = 0.03
print("The tuition for year 0 is:", tuition)
for i in range(5):
    tuition += tuition * rate
    print(f"The tuition for year {i+1} is: {tuition:.2f}")