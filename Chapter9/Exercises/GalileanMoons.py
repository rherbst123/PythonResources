# 1.  Galilean Moons of Jupiter
# Write a program that creates a dictionary containing the names of the Galilean moons of 
# Jupiter as keys and their mean radiuses (in kilometers) as values. The dictionary should 
# contain the following key-value pairs:
# Moon Name (key) Mean Radius (value)
# Io 1821.6
# Europa 1560.8
# Ganymede 2634.1
# Callisto 2410.3
# The program should also create a dictionary containing the moon names and their surface 
# gravities (in meters per second squared). The dictionary should contain the following key-
# value pairs: 
# Moon Name (key) Surface Gravity (value)
# Io 1.796
# Europa 1.314
# Ganymede 1.428
# Callisto 1.235
# The program should also create a dictionary containing the moon names and their orbital 
# periods (in days). The dictionary should contain the following key-value pairs:
# Moon Name (key) Orbital Period (value)
# Io 1.769
# Europa 3.551
# Ganymede 7.154
# Callisto 16.689

# The program should let the user enter the name of a Galilean moon of Jupiter, then it 
# should display the moon’s mean radius, surface gravity and orbital period


radius = {
    "Io" : 1821.6,
    "Europa": 1560.8,
    "Ganymede": 2634.1,
    "Callisto": 2410.3
}

surface_gravity = {
    "Io" : 1.796,
    "Europa": 1.313,
    "Ganymede": 1.428,
    "Callisto": 1.235
}

orbital_period = {
    "Io" : 1.796,
    "Europa": 3.551,
    "Ganymede": 7.154,
    "Callisto": 16.689
}

moon_choice = input("Enter the moon you want to learn about: ")


print(f"The moon {moon_choice}: Has a radius of {radius[moon_choice]} meters.")
print(f"{moon_choice} also has a surface gravity of {surface_gravity[moon_choice]},")
print(f"and a orbital period of {orbital_period[moon_choice]}")
