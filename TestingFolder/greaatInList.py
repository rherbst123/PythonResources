import random


def main():
    numbers = []
    for i in range(10):
        number = random.randint(1,100)
        numbers.append(number)
    
    
    findLargest(numbers)
    findSecondLargest(numbers)
    sortList(numbers)


def findLargest(numbers):
    
    i = 0
    largest = 0 
    for number in numbers:
        #print(numbers[i])
        if number > largest:
            largest = number
    print("Largest ",largest)
    return largest


def findSecondLargest(numbers):
    i = 0
    largest = 0
    secondLargest = 0
    for number in numbers:
        if number > largest:
            largest = number
    for number in numbers:
        if number > secondLargest and number != largest:
            secondLargest = number
    print("Second Largest",secondLargest)

    
def sortList(numbers):
    print(f"UnSorted{numbers}")
    size = len(numbers)
    #Bubble sort!
    for i in range(size): #as many iterations as there are entries in the list.
        #print(numbers)
        for j in range(size - i - 1):
            #print(numbers) #for indicies in the list, compare it to its neighbors, if larger then swap, 
            if numbers[j] > numbers[j + 1]:
                #print(numbers)
                numbers[j], numbers[j+1] =  numbers[j+1], numbers[j]
        

    

         
        
    print("Sorted",numbers)
        
        






main()