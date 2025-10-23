import matplotlib.pyplot as plt

def main():
    plt.xlim(xmin = 1, xmax = 100)
    plt.ylim(ymin = 1, ymax = 100)

    x = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    y = [0, 15, 35, 45, 60, 55, 70, 75, 85, 80, 95]

    plt.plot(x,y)

    plt.show()

main()