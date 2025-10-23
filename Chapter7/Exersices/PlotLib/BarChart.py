import matplotlib.pyplot as plt



def main():
    plt.title("WOW!")
    plt.xlabel("Things")
    plt.ylabel("And such")

    plt.xticks([0,1,2,3,4],[0,100,200,300,400])

    left = [0, 10, 20 , 30 , 40]
    height = [100, 200 , 300 , 400, 500]

    bar_width = 5
    plt.bar(left,height, bar_width)


    #plt.bar(left,height)
    
    
    plt.show()

main()