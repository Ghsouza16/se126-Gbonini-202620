"""
SE126 – 202520 - Make-Up Lab
Successful completion of this lab will replace one of your current lab grades.

This program allows users to search through student data from a file.
Version without os module - compatible with any system.
"""

# Global lists to store student data (1D parallel lists)
student_ids = []      # Student IDs
last_names = []       # Last names
first_names = []      # First names
class1 = []           # First class
class2 = []           # Second class
class3 = []           # Third class


def display_menu():
    """Display the menu and return user's choice"""
    print("\n" + "="*50)
    print("STUDENT DATABASE MENU")
    print("="*50)
    print("1. See All Student Report")
    print("2. Search for a Student [ID]")
    print("3. Search for a Student [Last Name]")
    print("4. View a Class Roster [class1, class2, and class3]")
    print("5. Exit/Quit Program")
    print("="*50)
    
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def load_data_from_file(filename):
    """
    Load student data from file into parallel lists
    File format: ID, LastName, FirstName, Class1, Class2, Class3
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                # Remove whitespace and split by comma
                data = line.strip().split(',')
                
                # Make sure we have all 6 fields
                if len(data) == 6:
                    student_ids.append(data[0].strip())
                    last_names.append(data[1].strip())
                    first_names.append(data[2].strip())
                    class1.append(data[3].strip())
                    class2.append(data[4].strip())
                    class3.append(data[5].strip())
        
        print(f"\nSuccessfully loaded {len(student_ids)} students from {filename}")
        return True
        
    except FileNotFoundError:
        print(f"\nError: File '{filename}' not found!")
        print("Please make sure 'students.txt' is in the same folder as this program.")
        return False
    except Exception as e:
        print(f"\nError reading file: {e}")
        return False


def display_all_students():
    """Display all student records (Option 1)"""
    if not student_ids:
        print("\nNo student data available.")
        return
    
    print("\n" + "="*80)
    print("COMPLETE STUDENT REPORT")
    print("="*80)
    print(f"{'ID':<10} {'Last Name':<15} {'First Name':<15} {'Class1':<12} {'Class2':<12} {'Class3':<12}")
    print("-"*80)
    
    for i in range(len(student_ids)):
        print(f"{student_ids[i]:<10} {last_names[i]:<15} {first_names[i]:<15} "
              f"{class1[i]:<12} {class2[i]:<12} {class3[i]:<12}")
    
    print("="*80)
    print(f"Total students: {len(student_ids)}")


def binary_search(search_item, search_type):
    """
    Binary search function for Options 2 & 3 (EXTRA CREDIT)
    search_type: 'id' or 'name'
    Returns index if found, -1 if not found
    """
    # Create a list of indices to sort by
    indices = list(range(len(student_ids)))
    
    # Sort indices based on search type
    if search_type == 'id':
        indices.sort(key=lambda i: student_ids[i])
        # Get sorted list of IDs for binary search
        sorted_items = [student_ids[i] for i in indices]
    else:  # search by last name
        indices.sort(key=lambda i: last_names[i].lower())
        # Get sorted list of last names for binary search
        sorted_items = [last_names[i].lower() for i in indices]
    
    # Convert search item to lowercase for case-insensitive search
    if search_type == 'name':
        search_item = search_item.lower()
    
    # Binary search algorithm
    low = 0
    high = len(sorted_items) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if sorted_items[mid] == search_item:
            # Found - return the original index
            return indices[mid]
        elif sorted_items[mid] < search_item:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Not found


def search_by_id():
    """Option 2: Search for a student by ID using binary search"""
    if not student_ids:
        print("\nNo student data available.")
        return
    
    print("\n" + "-"*40)
    search_id = input("Enter Student ID to search: ").strip()
    
    # Use binary search to find the student
    index = binary_search(search_id, 'id')
    
    if index != -1:
        print("\n" + "="*60)
        print("✓ STUDENT FOUND!")
        print("="*60)
        print(f"ID:        {student_ids[index]}")
        print(f"Last Name: {last_names[index]}")
        print(f"First Name: {first_names[index]}")
        print(f"Class 1:   {class1[index]}")
        print(f"Class 2:   {class2[index]}")
        print(f"Class 3:   {class3[index]}")
        print("="*60)
    else:
        print(f"\n✗ Student with ID '{search_id}' not found.")


def search_by_last_name():
    """Option 3: Search for a student by last name using binary search"""
    if not student_ids:
        print("\nNo student data available.")
        return
    
    print("\n" + "-"*40)
    search_name = input("Enter Last Name to search: ").strip()
    
    # Use binary search to find the student (case-insensitive)
    index = binary_search(search_name, 'name')
    
    if index != -1:
        print("\n" + "="*60)
        print("✓ STUDENT FOUND!")
        print("="*60)
        print(f"ID:        {student_ids[index]}")
        print(f"Last Name: {last_names[index]}")
        print(f"First Name: {first_names[index]}")
        print(f"Class 1:   {class1[index]}")
        print(f"Class 2:   {class2[index]}")
        print(f"Class 3:   {class3[index]}")
        print("="*60)
    else:
        print(f"\n✗ Student with last name '{search_name}' not found.")


def view_class_roster():
    """Option 4: View all students enrolled in a specific class using sequential search"""
    if not student_ids:
        print("\nNo student data available.")
        return
    
    print("\n" + "-"*40)
    search_class = input("Enter Class Name to search (e.g., MATH101, ENGLISH102): ").strip().lower()
    
    # List to store indices of students in the class
    found_indices = []
    
    # Sequential search through all three class lists
    for i in range(len(student_ids)):
        if (class1[i].lower() == search_class or 
            class2[i].lower() == search_class or 
            class3[i].lower() == search_class):
            found_indices.append(i)
    
    # Display results
    if found_indices:
        print("\n" + "="*60)
        print(f"CLASS ROSTER: {search_class.upper()}")
        print("="*60)
        print(f"{'ID':<10} {'Last Name':<15} {'First Name':<15}")
        print("-"*40)
        
        for index in found_indices:
            print(f"{student_ids[index]:<10} {last_names[index]:<15} {first_names[index]:<15}")
        
        print("="*60)
        print(f"Total students enrolled: {len(found_indices)}")
    else:
        print(f"\n✗ Class '{search_class}' not found.")


def main():
    """Main program function"""
    print("="*50)
    print("STUDENT DATABASE SYSTEM - MAKE-UP LAB")
    print("="*50)
    print("This lab can replace one previous lab grade.")
    print("Don't forget to comment which lab to replace in your Canvas submission!")
    
    # Load data from file
    if not load_data_from_file("students.txt"):
        print("\n" + "-"*40)
        input("Press Enter to exit...")
        return
    
    # Main program loop
    while True:
        choice = display_menu()
        
        if choice == 1:
            display_all_students()
        
        elif choice == 2:
            search_by_id()
        
        elif choice == 3:
            search_by_last_name()
        
        elif choice == 4:
            view_class_roster()
        
        elif choice == 5:
            print("\n" + "="*50)
            print("Thank you for using the Student Database System!")
            print("Goodbye!")
            print("="*50)
            break
        
        # Pause before showing menu again (except for exit)
        if choice != 5:
            input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()