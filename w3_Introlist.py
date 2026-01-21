#Week 3 demo - introduction to Id & parallel lists

#---IMPORTS-------------------------------------------------------------
import csv  #comma separated value
#---FUCTIONS-------------------------------------------------------------

#---MAIN EXECUTING CODE-------------------------------------------------------------
print("\n\tWelcome to lab #2 - Machine info Display")

total_records = 0

#working with lists --> 1 list for each potential field in the data file
machine_type = []   #creating an empty list
brand = []
proc = []
ram = []
first_hd = []
num_hd = []
second_hd = []
os = []
yr = []



print(f"{'TYPE':5}{'BRAND':10}{'PROC':4}{'RAM':7}{'1st HD':7}{'2nd HD':7}{'OS':5}{'YEAR':5}")
print("-"*50)
with open("filehandling.csv") as cvsfiles:

     file = csv.reader(cvsfiles)

     for rec in file:
        total_records += 1

        if rec[0] == "D":
            machine_type. append  ("Desktop")
        elif rec[0] == "L" :
            machine_type. append ("Laptop")
        else:
            machine_type. append ("ERROR")
       
       #rec[0] --> brand
     if rec[1] == "DL":
        brand = "DELL"
     elif rec[1]== "GW":
        brand = "Gateway"
     elif rec[1]== "HP":
        brand = "HP"
     else:
        brand. append ("ERROR")

        #rec[2] -- processor
        proc. append(rec[2])

        #rec[2] -- processor
        ram.append(rec[3])

        #rec[2] -- processor
        first_hd. append(rec[4])

        #rec[5] ..> KEY TO REST OF THE FIELDS!
        if rec[5] == "1":
            num_hd.append(rec[5])
            second_hd.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])
        else:
            num_hd.append(rec[5])
            second_hd.append(rec[6])
            os.append(rec[7])
            yr.append(rec[8])

            #display machine data
        #PROCESS THOUGHT THE LIST -- batch processing do the same thing to each  value in said list(s) --> for index in range (0, len(listname))
      #                                                                                                --> for index in listname:
      #PARALLEL LISTS: data organized in different lists, but connect via index
        for index in range(0, len(machine_type)):
          print(f"{machine_type[index]:10}{brand[index]:10}{proc[index]:4}{ram[index]:7}{first_hd[index]:7}{num_hd[index]:9}{second_hd[index]:7}{os[index]:5}{yr[index]:5}")
     print("- " * 50)

     old_desktops = 0
     old_laptops = 0

     for i in range(0, len(machine_type)):
        #count desktops and laptops that are too old (year -= 10)
        if int(yr[i]) <= 10:
                 #machine too old- now determine type for proper counting
                if machine_type[1] == "desktop":
                    old_desktops += 1
                elif machine_type[1] == "laptop":
                    old_laptops +=1
                else:
                    print(f"******* YOU HAVE AN ERROR IN INDEX {i} / data file line: {1+1}*****")

print("\n machines processed for replacement budget:")
print(f"desktops to replace: {old_desktops} @ $2k/each --> $ {old_desktops * 2000: .2f}")
print(f"desktops to replace: {old_laptops}@ $2k/each --> $ {old_laptops * 1500 :,.2f}")

total_cost = (old_desktops * 2000) + (old_laptops * 1500)
print(f"\n\t\t\tTotal replacement Cost: ${total_cost:.2f}")

    
    


        
print(f"\nTOTAL RECORDS: {total_records})\n\n Thank you for using my program goodbye:] \n\n\n")


