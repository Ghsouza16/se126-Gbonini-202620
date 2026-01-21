#Week 3 demo - introduction to Id & parallel lists

#---IMPORTS-------------------------------------------------------------
import csv  #comma separated value
#---FUCTIONS-------------------------------------------------------------

#---MAIN EXECUTING CODE-------------------------------------------------------------
print("\n\tWelcome to lab #2 - Machine info Display")

total_records = 0
print(f"{'TYPE':5}{'BRAND':10}{'PROC':4}{'RAM':7}{'1st HD':7}{'2nd HD':7}{'OS':5}{'YEAR':5}")
print("-"*50)
with open("text_file/files/filehandling.csv") as csvfille:

    file = csv . reader(csvfille)

    for rec in file:
        total_records += 1

        if rec[0] == "D":
            machine_type = "Desktop"
        elif rec[0] == "L" :
            machine_type = "Laptop"
        else:
            machine_type = "ERROR"
       
       #rec[1] --> brand
    if rec[1] == "DL":
        brand = "DELL"
    elif rec[1]== "GW":
        brand = "Gateway"
    elif rec[1]== "HP":
        brand = "HP"


