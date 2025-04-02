""" 5. Property Tax
 A county collects property taxes on the assessment value of property, which is 60 percent of 
the propertys actual value. For example, if an acre of land is valued at $10,000, its assess
ment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. 
The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the 
actual value of a piece of property and displays the assessment value and property tax. """


def taxCalculator(propertyVal):
    assesmentVal = propertyVal * 0.60

    propertyTax = (assesmentVal // 100) * 0.72

    assesmentVal = format(assesmentVal,"0.2f")
    propertyTax = format(propertyTax,"0.2f")

    return assesmentVal, propertyTax

propertyVal = float(input("Enter your property value: "))

assesmentVal, propertyTax = taxCalculator(propertyVal)
print(f"Assessment Value: ${assesmentVal}")
print(f"Property Tax: ${propertyTax}")


