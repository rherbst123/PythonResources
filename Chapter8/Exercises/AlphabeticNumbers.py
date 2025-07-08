# 5.  Alphabetic Telephone Number Translator
# Many companies use telephone numbers like 555-GET-FOOD so the number is easier for 
# their customers to remember. On a standard telephone, the alphabetic letters are mapped to 
# numbers in the following fashion:
# A, B, and C = 2
# D, E, and F = 3
# G, H, and I = 4
# J, K, and L = 5
# M, N, and O = 6
# P, Q, R, and S = 7
# T, U, and V = 8
# W, X, Y, and Z = 9
# Write a program that asks the user to enter a 10-character telephone number in the for-
# mat XXX-XXX-XXXX. The application should display the telephone number with any 
# alphabetic  characters  that  appeared  in  the  original  translated  to  their  numeric  equiva-
# lent.  For  example,  if  the  user  enters  555-GET-FOOD,  the  application  should  display  
# 555-438-3663.



def conversion(phone_number):
    conversions = [("A","B","C",2),("D","E","F",3),("G","H","I",4),
                   ("J","K","L",5),("M","N","O",6),("P","Q","R","S",7),
                   ("T","U","V",8),("W","X","Y","Z",9)]
    
    translated_number = ""
    for ch in phone_number.upper():
        #Is Alpha Numeric
        if ch.isalpha():
            #For (things) in [list] if the Capitolized char is in the (things)
            for group in conversions:
                #Turns out the (things) is named (group)
                if ch in group[:-1]:  # Check if the character is in the group
                    #Append the individual bits
                    translated_number += str(group[-1])  # Append the corresponding number
                    break
        else:
            translated_number += ch  # Append non-alphabetic characters as is

    print(translated_number)


def main():
    phone_number = input("Enter a XXX-XXX-XXXX phone number with a catchy last 7 digits: ")

    conversion(phone_number)
main()