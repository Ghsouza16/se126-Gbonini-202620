#Guilherme
#lab 1

#Prompt
# You will be writing one Python file for this project - it is a program that determines whether a
# meeting room is in violation of fire regulations regarding the maximum room capacity. The 
# program will accept the maximum room capacity and the number of people attending the
# meeting. If the number of people is less than or equal to the maximum room capacity, the
# program announces that it is legal to hold the meeting and tells how many additional people may
# legally attend. If the number of people exceeds the maximum room capacity, the program
# announces that the meeting cannot be held as planned due to the fire regulation and tells how
# many people must be excluded in order to meet the fire regulations. The user should be allowed
# to enter and check as many rooms as they would like without exiting the program.


#--FUNCTIONS-------------------------------------------
#function definition below - must define before calling in main code (using)
def difference(people: int, max_cap: int) -> int:
    """Return max_cap - people. Positive -> seats remaining; negative -> over capacity."""
    return max_cap - people


def decision() -> str:
    """Ask the user whether they want to check another room. Returns 'y' or 'n'."""
    while True:
        answer = input("\t\tWould you like to check another room? [y/n]: ").strip().lower()
        if answer in ("y", "n"):
            return answer
        print("INVALID ENTRY - please enter 'y' or 'n'.")


#----MAIN CODE-------------------------------------------

#function call below - actually the function
print("\n\t\tWelcome to my lab #1\n")


def main() -> None:
    print(f"the difference is: {difference(22, 25)}")  # example/test line - optional

    answer = "y"
    while answer == "y":
        # asks a user for the meeting name, room capacity, and people attending the meeting
        name = input("\nEnter the name of the room: ").strip()

        # validate numeric input for capacity and attending
        try:
            capacity = int(input(f"Enter the max capacity for {name} room: "))
            attending = int(input(f"Enter the number of people attending the meeting in {name} room: "))
        except ValueError:
            print("Invalid number entered. Please enter integer values for capacities and attendees.")
            continue

        # compute difference
        diff_return = difference(attending, capacity)
        if diff_return >= 0:
            print("\nThe meeting can be held legally")
            print(f"{diff_return} additional people can legally attend")
        else:
            print("\nThe meeting will be illegal as planned")
            print(f"{abs(diff_return)} people must be excluded to meet the fire regulations.")

        # ask if user wants to check another room
        answer = decision()

    print("\nThank you — goodbye!")


if __name__ == "__main__":
    main()