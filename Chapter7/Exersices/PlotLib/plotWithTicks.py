import matplotlib.pyplot as plt

def main():
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 2, 3, 4]

    plt.xticks([0,1,2,3,4],['2016','2017','2018','2019','2020'])
   
    plt.yticks([0,1,2,3,4,5],['$0m','$1m','$2m','$3m','$4m','$5m'])

    plt.plot(x,y)
    
    plt.title('sales by year')

    plt.xlabel("year")
    plt.ylabel("Sales")

    plt.show()

main()