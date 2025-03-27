"""  You have a group of friends coming to visit for your high school reunion, and you want 
to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary 
restrictions, but your restaurant choices are as follows:
 Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No
 Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
 Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
 Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No
 The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
 Write a program that asks whether any members of your party are vegetarian, vegan, or 
gluten-free, to which then displays only the restaurants to which you may take the group. 
Here is an example of the program’s output:
 Is anyone in your party a vegetarian? yes Enter
 Is anyone in your party a vegan? no Enter
 Is anyone in your party gluten-free? yes Enter
 Here are your restaurant choices:
   Main Street Pizza Company
   Corner Cafe
   The Chef's Kitchen
 Here is another example of the program’s output:
 Is anyone in your party a vegetarian? yes Enter
 Is anyone in your party a vegan? yes Enter
 Is anyone in your party gluten-free? yes Enter
 Here are your restaurant choices:
   Corner Cafe
   The Chef's Kitche """

message = ""

vegetarian = input("Is anyone in your party a vegetarian? ")

if vegetarian == "yes" or vegetarian == "no":
    vegan = input("Is anyone in your party a vegan? ")

    if vegan == "yes" or vegan == "no":
        gluten_free = input("Is anyone in your party gluten-free? ")

        if gluten_free == "yes" or gluten_free == "no":
            message = "\nHere are your restaurant choices:\n"

            if vegetarian == "yes":
                
                if vegan == "yes":

                    if gluten_free == "yes" or gluten_free == "no":
                        message += "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                else: 
                    if gluten_free == "yes":
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                    else:
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"
            else: # vegetarian == "no"

                if vegan == "yes":

                    if gluten_free == "yes" or gluten_free == "no":
                        message += "Corner Cafe\nThe Chef's Kitchen\n"

                else: # vegan == "no"

                    if gluten_free == "yes":
                        message += "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "The Chef's Kitchen\n"
                                   
                    else: # gluten free == "no"
                        message += "Joe's Gourmet Burgers\n" + \
                                   "Main Street Pizza Company\n" + \
                                   "Corner Cafe\n" + \
                                   "Mama's Fine Italian\n" + \
                                   "The Chef's Kitchen\n"

        else:
            message = "Enter either 'yes' or 'no'.\nRerun the program and try again."
    
    else:
        message = "Enter either 'yes' or 'no'.\nRerun the program and try again."

else:
    message = "Enter either 'yes' or 'no'.\nRerun the program and try again."


print(message)