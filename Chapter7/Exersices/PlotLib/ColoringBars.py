import matplotlib.pyplot as plt



def main():
    left = [0, 10, 20 , 30 , 40]
    height = [100, 200 , 300 , 400, 500]

    bar_width = 5
    plt.bar(left, height, color=('r','g','b','m','k'), width=bar_width)


    #plt.bar(left,height)
    
    
    plt.show()

main()