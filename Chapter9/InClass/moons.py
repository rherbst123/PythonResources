moon_radius = {
        "Io": 1821.6,
        "Europa": 1560.8,
        "Ganymede": 2634.1,
        "Callisto": 2410.3
}

surface_gravity = {
        "Io": 1.796,
        "Europa": 1.314,
        "Ganymede": 1.428,
        "Callisto": 1.235
}

orbital_period = {
        "Io": 1.796,
        "Europa": 3.551,
        "Ganymede": 7.154,
        "Callisto": 16.689  
}


moon_choice = input("Enter the moon you want to learn about: ")

print(f"The moon, {moon_choice}: Has a radious of {moon_radius[moon_choice]}, kilometers")
print(f"the moon, {moon_choice} also has a surface gravity of {surface_gravity[moon_choice]}")
print(f"and a orbital period of: {orbital_period[moon_choice]}")





