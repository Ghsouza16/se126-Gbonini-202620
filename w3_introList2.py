#Week 3 Demo - Introduction to 1D & Parallel Lists

#---IMPORTS--------------------------------------------------------
import csv      #comma  seperated  value
#---FUNCTIONS------------------------------------------------------

#---MAIN EXECUTING CODE--------------------------------------------
print("\n\tWelcome to Lab #2 - Machine Info Display\t")

total_records = 0       #in future can use: len(listName) to get length

#working with lists -> 1 list for EACH POTENTIAL FIELD in the data file
machine_type = []   #creating an empty list
brand = []
proc = []
ram = []
first_hd = []
num_hd = []
second_hd = []
os = []
yr = []

#print(f"{'TYPE':10}{'BRAND':10}{'PROC':4}{'RAM':7}{'1st HD':7}{'#HD':5}{'2nd HD':7}{'OS':5}{'YEAR':5}")
#print("-" * 50)
with open("filehandling.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:
        total_records += 1

        #rec[0] --> machine_type
        if rec[0] == "D": 
            machine_type.append("Desktop")
        elif rec[0] == "L":
            machine_type.append("Laptop")
        else:
            machine_type.append("*ERROR*")

        #rec[1] --> brand
        if rec[1] == "DL":
            brand.append("Dell")
        elif rec[1] == "GW":
            brand.append("Gateway")
        elif rec[1] == "HP":
            brand.append("HP")
        else:
            brand.append("*ERROR*")

        #rec[2] --> processor
        proc.append(rec[2])

        #rec[3] --> RAM
        ram.append(rec[3])

        #rec[4] --> first_hd
        first_hd.append(rec[4])

        #rec[5] --> KEY TO REST OF THE FIELDS! --> num_hd
        if rec[5] == "1":
            num_hd.append(rec[5])
            second_hd.append("---") #no second hard drive!
            os.append(rec[6])
            yr.append(rec[7])
        else:
            num_hd.append(rec[5])
            second_hd.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])

        #display machine data
        #print(f"{machine_type:10}{brand:10}{proc:4}{ram:7}{first_hd:7}{num_hd:5}{second_hd:7}{os:5}{yr:5}")
#print("-" * 50)
#disconnected from file--------------------

#PROCESS THROUGH THE LISTS -- batch processing: do the same thing to each value in said list(s) --> for index in range(0, len(listName)):
#                     --> for index in listName:
#PARALLEL LISTS: data organized in different lists, but connected via index
print(f"{'TYPE':10}{'BRAND':10}{'PROC':4}{'RAM':7}{'1st HD':7}{'#HD':5}{'2nd HD':7}{'OS':5}{'YEAR':5}")
print("-" * 50)
for index in range(0, len(machine_type)):
    print(f"{machine_type[index]:10}{brand[index]:10}{proc[index]:4}{ram[index]:7}{first_hd[index]:7}{num_hd[index]:5}{second_hd[index]:7}{os[index]:5}{yr[index]:5}")
print("-" * 50)

old_desktops = 0
old_laptops = 0 

for i in range(0, len(machine_type)): 
    #count desktops and laptops that are too old (year <= 16)
    if int(yr[i]) <= 16:
        #machine too old - now determine type for proper counting
        if machine_type[i] == "Desktop":
            old_desktops += 1
        elif machine_type[i] == "Laptop":
            old_laptops += 1
        else:
            print(f"****YOU HAVE AN ERROR IN index {i} / data file line: {i + 1}****")

print("\nMachines processed for replacement budget:")
print(f"\tDesktops to replace: {old_desktops}  @ $2k/each  --> ${old_desktops * 2000:.2f}")
print(f"\t Laptops to replace: {old_laptops}  @ $1.5k/each --> ${old_laptops * 1500:.2f}")

total_cost = (old_desktops * 2000) + (old_laptops * 1500)
print(f"\n\t\t\tTotal Replacement Cost: ${total_cost:,.2f}")

print(f"\nTOTAL RECORDS: {total_records}\n\nThank you for using my program Goodbye. \n\n\n")