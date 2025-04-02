"""  15. Write a program that uses nested loops to draw this pattern:
 ##
 # #
 #  #
 #   #
 #    #
 #     # """

star = "#"
space = " "
spaceNum = 0


for i in range(7):
    print(f"{star}{spaceNum*space}{star}")
    spaceNum += 1