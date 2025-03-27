"""  Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. Use 
the flowchart to create a program that leads a person through the steps of fixing a bad 
Wi-Fi connection. Here is an example of the program’s output:
refer to https://www.kalfaoglu.com/ceng113/Python-Programming/Starting%20Out%20with%20Python%5B4th%20Globa%20lED%5DTony%20Gaddis.pdf Page: 177-178

 """

shoots = [" Reboot the computer and try to connect"," Reboot the router and try to connect."," Make sure the cablesbetween the router & modemare plugged in firmly."," Move the router to a new location and try to connect.", " Get a new router."]

shootsLen = len(shoots)
print(shoots[0])
userSays = input("Did that fix the problem?: (y/n): ")

#print(shoots[0])
if userSays == "n":
    print(shoots[1])
    userSays = input("Did that fix the problem?: (y/n): ")
    if userSays == "n":
        print(shoots[2])
        userSays = input("Did that fix the problem?: (y/n): ")
        if userSays == "n":
            print(shoots[3])
            userSays = input("Did that fix the problem?: (y/n): ")
            if userSays == "n":
                print(shoots[4])
                exit()

