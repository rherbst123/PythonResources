import matplotlib.pyplot as plt

def main():

    x = [0,1,2,3,4]
    y = [0,3,1,5,2]

    plt.plot(x,y)
    
    plt.title('sales by year')

    plt.xlabel("year")
    plt.ylabel("Sales")

    plt.show()

main()