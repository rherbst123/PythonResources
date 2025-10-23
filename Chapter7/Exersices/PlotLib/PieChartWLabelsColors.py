import matplotlib.pyplot as plt


def main():
    values = [20,60,80,40]
    labels = ['1st Qtr', '2nd Qtr', '3rd Qtr', '4th Qtr']
    plt.title("Sales")
    plt.pie(values, labels=labels,  colors=('r', 'g', 'b', 'k'))

    plt.show()

main()