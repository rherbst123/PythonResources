""" 15. Time Calculator
 Write a program that asks the user to enter a number of seconds and works as follows:
 •	There	are	60	seconds	in	a	minute.	If	the	number	of	seconds	entered	by	the	user	is	greater	
than or equal to 60, the program should convert the number of seconds to minutes and 
seconds.
 •	There are 3,600 seconds in an hour. If the number of seconds entered by the user is 
greater than or equal to 3,600, the program should convert the number of seconds to 
hours, minutes, and seconds.
 •	There are 86,400 seconds in a day. If the number of seconds entered by the user is 
greater than or equal to 86,400, the program should convert the number of seconds to 
days, hours, minutes, and seconds """

seconds = int(input("Enter seconds:" ))

if seconds > 60 and seconds < 3600:
    print(seconds // 60)
if seconds > 3599 and seconds < 86400:
    hours = seconds // 60 // 60
    minutes = hours // 60
    seconds = minutes // 60
    print("Hours:", hours, "Minutes:", minutes, "Seconds: ", seconds)
if seconds > 86399:
    days = seconds // 60 // 60 // 24
    hours = seconds // 60 // 60
    minutes = hours // 60
    seconds = minutes // 60
    print("Days: ", days, "Hours:", hours, "Minutes:", minutes, "Seconds: ", seconds)

    