# Midterm Choice 1 - Employee Management System (Exact Assignment Requirements)


#---IMPORTS--------------------------------------------------------
import csv
#---MAIN EXECUTING CODE--------------------------------------------
print("\n" + "=" * 60)
print("\tEmployee Management System")
print("=" * 60)

# Parallel lists
first_names = []
last_names = []
emails = []
departments = []
phone_extensions = []
office_numbers = []

total_records = 0

# Read from westeros (1).csv
try:
    with open("westeros (1).csv") as csvfile:
        file = csv.reader(csvfile)
        
        for rec in file:
            total_records += 1
            first_names.append(rec[0])
            last_names.append(rec[1])
            emails.append(rec[2])
            departments.append(rec[3])
            phone_extensions.append(rec[4])  # Using as phone extension
            
except FileNotFoundError:
    print("ERROR: File 'westeros (1).csv' not found!")
    exit()

# Assign office numbers (100-200)
next_office = 100
for i in range(total_records):
    if next_office > 200:
        office_numbers.append("N/A")
    else:
        office_numbers.append(str(next_office))
        next_office += 1

# Display all data
print(f"\n{'FIRST':12}{'LAST':12}{'EMAIL':25}{'DEPT':20}{'PHONE':12}{'OFFICE':10}")
print("-" * 90)

for i in range(total_records):
    print(f"{first_names[i]:12}{last_names[i]:12}{emails[i]:25}{departments[i]:20}{phone_extensions[i]:12}{office_numbers[i]:10}")

print("-" * 90)
print(f"\nTOTAL RECORDS: {total_records}")

# Write to midterm_choice1.csv
with open("midterm_choice1.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["First", "Last", "Email", "Department", "Phone", "Office"])
    for i in range(total_records):
        writer.writerow([first_names[i], last_names[i], emails[i], 
                        departments[i], phone_extensions[i], office_numbers[i]])

print("\nData written to 'midterm_choice1.csv'")

# Search Program
print("\n" + "=" * 60)
print("\tEmployee Directory Search")
print("=" * 60)

def search_email():
    email = input("\nEnter email to search: ").strip().lower()
    for i in range(total_records):
        if emails[i].lower() == email:
            print(f"\nEmployee Found:")
            print(f"  Name: {first_names[i]} {last_names[i]}")
            print(f"  Email: {emails[i]}")
            print(f"  Department: {departments[i]}")
            print(f"  Phone: {phone_extensions[i]}")
            print(f"  Office: {office_numbers[i]}")
            return
    print(f"\nNo employee with email: {email}")

def search_department():
    dept = input("\nEnter department to search: ").strip()
    found = []
    for i in range(total_records):
        if departments[i].lower() == dept.lower():
            found.append(i)
    
    if found:
        print(f"\nFound {len(found)} employee(s) in {dept}:")
        print(f"{'NAME':20}{'EMAIL':25}{'PHONE':12}{'OFFICE':10}")
        print("-" * 67)
        for idx in found:
            name = f"{first_names[idx]} {last_names[idx]}"
            print(f"{name:20}{emails[idx]:25}{phone_extensions[idx]:12}{office_numbers[idx]:10}")
    else:
        print(f"\nNo employees in department: {dept}")

# Main menu loop
while True:
    print("\n" + "-" * 40)
    print("SEARCH MENU")
    print("1. Search by EMAIL")
    print("2. Search by DEPARTMENT")
    print("3. EXIT")
    print("-" * 40)
    
    choice = input("Enter choice (1-3): ").strip()
    
    if choice == "1":
        search_email()
    elif choice == "2":
        search_department()
    elif choice == "3":
        print("\nGoodbye!")
        break
    else:
        print("Invalid choice. Enter 1, 2, or 3.")
    
    if choice != "3":
        input("\nPress Enter to continue...")

print("\nProgram completed.")