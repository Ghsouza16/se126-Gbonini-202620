#GB
#Lab 1
#1-6-2026

#PROGRAM PROMPT: ou will be writing one Python file for this project - it is a program that determines whether a meeting room is in violation of fire regulations regarding the maximum room capacity. The program will accept the maximum room capacity and the number of people attending the meeting. If the number of people is less than or equal to the maximum room capacity, the program announces that it is legal to hold the meeting and tells how many additional people may legally attend. If the number of people exceeds the maximum room capacity, the program announces that the meeting cannot be held as planned due to the fire regulation and tells how many people must be excluded in order to meet the fire regulations. The user should be allowed to enter and check as many rooms as they would like without exiting the program.


#---FUNCTIONS--------------------------------
#function definition below - must define before calling in main code (using)
def difference(people, max_cap):

    diff = max_cap - people 

    #the return value LITERALLY replaces the function call 
    return diff #when diff < 0, too many ppl for room


def decision(a):

    #error trap loops! 
    while a != "y" and a != "n":
        print("***INVALID ENTRY - 'y' or 'n' only!")
        a = input("\t\tWould you like to check another room? [y/n]: ").lower()

    return a
#---MAIN CODE--------------------------------

#function call below - actually the function
print(f"The difference is: {difference(22, 25)}")

print("\n\t\tWelcome to my Lab #1\n")

answer = "y"

while answer == "y":

    #asks a user for the meeting name, room capacity, and people attending the meeting
    name = input("\nEnter the name of the room: ")
    capacity = int(input(f"Enter the max capacity for {name} room: "))
    attending = int(input(f"Enter the number of people attending the meeting in {name} room: "))

    #passes the room capacity and people attending to the difference() you wrote in Part 1
    diff_return = difference(attending, capacity)

    #displays to the user whether the meeting meets fire safety or not (legal/illegal)
    #also display how many people can be added or removed (remember: if different returns a negative number, this is how many people should be removed) NOTE: all values related to people (adding/removing) should be displayed as positive values
 
    if diff_return >= 0:
            print("\nThe meeting can be held legally")
            print(f"{diff_return} additional people can legally attend")
    else:
            print("\nThe meeting will be illegal")
            print(f"{abs(diff_return)} people must be excluded to meet the fire regulations.")

        # ask if user wants to check another room
    answer = decision(answer) 
    #if diff_return > 0: .... 




    #ask the user if they have another number to check; pass the value to the decision() you wrote inPart 2 and continue the program based on that function’s return
    answer = input("\t\tWould you like to check another room? [y/n]: ").lower()

    answer = decision(answer)

#Once the user is done checking meeting attendance, display a goodbye message


