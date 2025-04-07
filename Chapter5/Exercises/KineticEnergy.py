# 14. Kinetic Energy
#  In physics, an object that is in motion is said to have kinetic energy. The following formula 
# can be used to determine a moving object’s kinetic energy:
#  KE  = ½mv2
#  The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass 
# in kilograms, and v is the object’s velocity in meters per second.
#  Write a function named kinetic_energy that accepts an object’s mass (in kilograms) 
# and velocity (in meters per second) as arguments. The function should return the amount 
# of kinetic energy that the object has. Write a program that asks the user to enter values 
# for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic 
# energy.

def main():
    mass = int(input("Enter your objects mass: "))
    velocity = int(input("What is the veloity of the object?: "))
    
    ke = energy(mass, velocity)
    print(f"The object has a kinetic enetry of {ke}")
    return 0


def energy(mass, velocity):
    
    ke = 0.5 * mass * velocity ** 2
    
    return ke

main()