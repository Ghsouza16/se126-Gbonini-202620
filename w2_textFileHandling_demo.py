#W2 - Text file handling Intro demo

#STEP 1: import the CSV (comma separeted value) library
import csv

total_records = 0 #holds total num of recs in file

#STEP 2: connect to file
#--connected to file--------------------------------------
 #include relative file ath in open() - make sure to switch \ to /
with open("simple.csv") as csvfile:
   #make sure to indent inside of code block

   #allow the csv reader to access and read the file
   file = csv.reader(csvfile)
   #file - entires data from file organize as records

   #STEP 3: processs through every record (row) in the file
for record in file:
   #add +1 to total_records to keep accurate count
   total_records += 1 #total_records = total_records +1 
   print(record) #entire record/row data as a list

   name = record(0) #name field
   number = record(1) #number field
   color = record(2) #color field

print(f"{name}'s number is {number} and they love the color {color}!")


 #--disconnected from file----------------------------------------------------

print("--------------------------------------------")
print(f"\nTOTAL RECORDS: {total_records}\n")