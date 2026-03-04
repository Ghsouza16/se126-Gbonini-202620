#DICTIONARIES:another collection type in ython (like: lists)

import csv 
#dictionary -> {}
library={
    #indexes are STRINGS set by the developer
    #'KEY' : values,
    '1230' : "Red Rising",
    '1231' : "The Little Prince"
}
print(f"library['1230'] : {library['1230']}")


#list -> []
library_nums = []
     #'1234', #-->[0]
    #'1235'  #-->[1]

library_nums[0] print(f"library_nums[0]: {library_nums[0]}") #--> "1234"

titles=[]

with open ('library_books.csv') as csvfile:
    file=csv.reader(csvfile)

    for rec in file:
        library_nums.append(rec[0])
        titles.append(rec[1])


        #add each record's data as nek KEY + VALUE pair from the text file
        #key --> rec[0], value --> rec[1]
        library.update({rec[0]: rec[1]})

    #disconnect from file-------------------------------------------

    print(f"\n{'LIBRARY NUM'}\t{'TITLE'}")
    print("-" *50)
    for i in range(0, len(titles)):
        print(f"\n{library_nums[i]:11}\t{titles[1]}")
        print("-" *50)
        


#BINARY SEARCH for a library NUM - using LISTS!
min=0#reps the first possible index
max=len(titles) - 1 #reps the last possible index
mid=min+max//2 #middle index between min&msn
               # // FLOOR --> removes the decimal


Search = input("\nEnter the LIBRARY NUM you are loking for:")

while min<max and Search != titles[mid]:
    if Search < titles[mid]:
        max = mid - 1
    else:
        min = mid +1

    mid = min+max //2