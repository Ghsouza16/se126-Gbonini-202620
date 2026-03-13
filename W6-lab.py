# Lab #6: Airplane Seating Chart
# SE126 - 202520
# Author: [Your Name]
# Date: [Current Date]
# 
# Description: This program manages an airplane seating chart using a 2D list.
# It allows users to view available seats and reserve seats by row and seat number.
# The seating chart updates in real-time after each reservation.

# ================ INITIALIZATION ================
# Create a 2D list representing the airplane seating
# Row 1: Seats A, B, C, D
# Row 2: Seats A, B, C, D
# Row 3: Seats A, B, C, D
# Row 4: Seats A, B, C, D
# Row 5: Seats A, B, C, D
# Row 6: Seats A, B, C, D
# Row 7: Seats A, B, C, D

# Option 1: Hand-populated seating chart
seating_chart = [
    ['A', 'B', 'C', 'D'],  # Row 1
    ['A', 'B', 'C', 'D'],  # Row 2
    ['A', 'B', 'C', 'D'],  # Row 3
    ['A', 'B', 'C', 'D'],  # Row 4
    ['A', 'B', 'C', 'D'],  # Row 5
    ['A', 'B', 'C', 'D'],  # Row 6
    ['A', 'B', 'C', 'D']   # Row 7
]

# Option 2: To use a file instead, uncomment the code below:
"""
def load_seating_from_file(filename):
    # Load seating chart from a file
    seating = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Convert each line to a list of seat markers
                row = line.strip().split(',')
                seating.append(row)
    except FileNotFoundError:
        print(f"File {filename} not found. Using default seating.")
        # Default seating if file not found
        seating = [['A', 'B', 'C', 'D'] for _ in range(7)]
    return seating

# Load from file (you would need to create this file)
# seating_chart = load_seating_from_file('seating.txt')
"""

# ================ FUNCTIONS ================

def display_seating_chart(chart):
    """
    Displays the airplane seating chart in a neat, formatted way.
    
    Parameters:
        chart (2D list): The current seating chart
    
    Returns:
        None
    """
    print("\n" + "=" * 50)
    print("AIRPLANE SEATING CHART")
    print("=" * 50)
    
    # Print column headers
    print("     ", end="")
    for seat_letter in ['A', 'B', 'C', 'D']:
        print(f"  {seat_letter}  ", end="")
    print("\n")
    
    # Print each row
    for i in range(len(chart)):
        # Print row number
        print(f"Row {i+1}: ", end="")
        
        # Print each seat in the row
        for j in range(len(chart[i])):
            seat = chart[i][j]
            if seat == 'X':
                # Reserved seat
                print(f" [X] ", end="")
            else:
                # Available seat
                print(f" [{seat}] ", end="")
        print()  # New line after each row
    
    print("=" * 50)
    print("KEY: [X] = Reserved, [A/B/C/D] = Available")
    print("=" * 50 + "\n")

def is_valid_seat(chart, row, seat_letter):
    """
    Checks if the selected seat is valid and available.
    
    Parameters:
        chart (2D list): The current seating chart
        row (int): The selected row number
        seat_letter (str): The selected seat letter
    
    Returns:
        bool: True if seat is valid and available, False otherwise
    """
    # Check if row is valid (1-7)
    if row < 1 or row > len(chart):
        print(f"❌ Error: Row {row} is invalid. Please choose a row between 1 and {len(chart)}.")
        return False
    
    # Convert seat letter to uppercase for consistency
    seat_letter = seat_letter.upper()
    
    # Check if seat letter is valid (A, B, C, D)
    valid_seats = ['A', 'B', 'C', 'D']
    if seat_letter not in valid_seats:
        print("❌ Error: Invalid seat letter. Please choose A, B, C, or D.")
        return False
    
    # Check if seat is available (not 'X')
    seat_index = valid_seats.index(seat_letter)
    if chart[row-1][seat_index] == 'X':
        print(f"❌ Error: Row {row}, Seat {seat_letter} is already reserved.")
        return False
    
    return True

def reserve_seat(chart, row, seat_letter):
    """
    Reserves a seat by marking it as 'X'.
    
    Parameters:
        chart (2D list): The current seating chart
        row (int): The selected row number
        seat_letter (str): The selected seat letter
    
    Returns:
        bool: True if reservation was successful, False otherwise
    """
    # Validate the seat first
    if not is_valid_seat(chart, row, seat_letter):
        return False
    
    # Convert seat letter to uppercase
    seat_letter = seat_letter.upper()
    
    # Find the column index for the seat letter
    valid_seats = ['A', 'B', 'C', 'D']
    seat_index = valid_seats.index(seat_letter)
    
    # Reserve the seat
    chart[row-1][seat_index] = 'X'
    
    print(f"✅ Success! Row {row}, Seat {seat_letter} has been reserved.")
    return True

def get_available_seats_count(chart):
    """
    Counts the number of available seats in the chart.
    
    Parameters:
        chart (2D list): The current seating chart
    
    Returns:
        int: Number of available seats
    """
    count = 0
    for row in chart:
        for seat in row:
            if seat != 'X':
                count += 1
    return count

def display_menu():
    """
    Displays the main menu options.
    
    Parameters:
        None
    
    Returns:
        None
    """
    print("\n" + "-" * 40)
    print("MAIN MENU")
    print("-" * 40)
    print("1. View Seating Chart")
    print("2. Reserve a Seat")
    print("3. Exit")
    print("-" * 40)

# ================ MAIN PROGRAM ================

def main():
    """
    Main program function that runs the airplane seating reservation system.
    
    Parameters:
        None
    
    Returns:
        None
    """
    print("\n" + "#" * 60)
    print("#        AIRPLANE SEATING RESERVATION SYSTEM        #")
    print("#" * 60)
    
    # Create a copy of the seating chart to work with
    current_chart = [row[:] for row in seating_chart]
    
    # Main program loop
    running = True
    while running:
        display_menu()
        
        # Get user choice
        try:
            choice = input("Enter your choice (1-3): ").strip()
            
            if choice == '1':
                # View seating chart
                display_seating_chart(current_chart)
                available = get_available_seats_count(current_chart)
                print(f"📊 Available seats: {available} out of 28")
                
            elif choice == '2':
                # Reserve a seat
                print("\n--- Reserve a Seat ---")
                
                # Show current seating for reference
                display_seating_chart(current_chart)
                
                try:
                    # Get row number
                    row = int(input("Enter row number (1-7): "))
                    
                    # Get seat letter
                    seat = input("Enter seat letter (A, B, C, D): ").strip()
                    
                    # Attempt to reserve the seat
                    reserve_seat(current_chart, row, seat)
                    
                except ValueError:
                    print("❌ Error: Please enter a valid number for the row.")
                    
            elif choice == '3':
                # Exit program
                print("\n👋 Thank you for using the Airplane Seating Reservation System!")
                print(f"Final seating chart:")
                display_seating_chart(current_chart)
                print("Goodbye!")
                running = False
                
            else:
                print("❌ Error: Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Exiting...")
            running = False

# Call the main function to start the program
if __name__ == "__main__":
    main()