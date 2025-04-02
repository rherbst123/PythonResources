"""  13. Falling Distance
 When an object is falling because of gravity, the following formula can be used to deter
mine the distance the object falls in a specific time period:

    d = 1/2 gt^2

 The variables in the formula are as follows: d is the distance in meters, g is 9.8, and t is the 
amount of time, in seconds, that the object has been falling.
 Write a function named falling_distance that accepts an object’s falling time (in seconds) 
as an argument. The function should return the distance, in meters, that the object has  
fallen during that time interval. Write a program that calls the function in a loop that passes 
the values 1 through 10 as arguments and displays the return value. """


def main():
    time = int(input("How much time has passed: "))
    
    distance = physics(time)

    print(f"the object has fallen {distance}")
    return 0


def physics(time):
    gravity = 9.8
    for t in range(1, int(time) + 1):
        distance = 0.5 * gravity * t ** 2 #d = 1/2 gt^2
        print(f"At {t} seconds, the object has fallen {distance:.2f} meters")


main()