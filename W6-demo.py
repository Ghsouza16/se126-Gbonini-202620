#W6- Searching algorithms: Binary vs Sequetinal search
import csv

library_nums = []
titles=[]
authors=[]
genres=[]
pages=[]

with open("library_books.csv") as csvfile:
    file= csv.reader(csvfile)

    for rec in file:
        library_nums.append(rec[0])
        titles.append(rec[1])
        authors.append(rec[2])
        genres.append(rec[3])
        pages.append(rec[4])

        print(f"{'line':5} {'title':25} {'author':15} {'genre':20} {'pages':5}")
        print("---------------------------------------------------------------------")
        for i in range(0, len(library_nums)):
            print(f"{library_nums[i]:5} {titles[i]:25} {authors[i]:15} {genres[i]:20} {pages[i]:5}")
print("-----------------------------------------------------------------------------")

#SEQUENTIAL SEARCH: allow a user to search for a specific title
#titles[] is not ordered
found=[]
search_titles= input("which titles are you looking for:")
seq_count= 0

for i in range(0, len(titles)):
    seq_count += 1

    if search_titles in titles[i]:
        found.append(i)

print(f"SEARCH INTERATIONS: {seq_count}")

if not found: #"if the list found is empty"
    #found lists is still empty, meaning no matches to our search term were found
    print(f"Sorry, your search for {search_titles}was not found")
else:
    print(f"{'line':5} {'title':25} {'author':15} {'genre':20} {'pages':5}")
    print("---------------------------------------------------------------------")
    for i in range(0, len(library_nums)):
            print(f"{library_nums[1]:5} {titles[1]:25} {authors[1]:15} {genres[1]:20} {pages[1]:5}")
print("-----------------------------------------------------------------------------")


#Binary Search Algorithm:

search_num = input("Get search from user!")
min = 0
max = len(library_nums) - 1       

mid =  int((min + max) / 2)

bin_count = 0
#this is for INCREASING order
while (min < max and search_num != library_nums[mid]):

   if search_num < library_nums[mid]:
       max = mid - 1

   else:
       min = mid + 1

   mid = int((min + max) / 2)

if search_num == library_nums[mid]:
        print(f"Sorry, your search for {search_num}was not found")
else:
    print(f"{'line':5} {'title':25} {'author':15} {'genre':20} {'pages':5}")
    print("---------------------------------------------------------------------")
    for i in range(0, len(library_nums)):
            print(f"{library_nums[1]:5} {titles[1]:25} {authors[1]:15} {genres[1]:20} {pages[1]:5}")
print("-----------------------------------------------------------------------------")


    #found them! use 'guess' for index of found search item
else: 
print(f"Sorry<your search for{search_titles} was NOt found")


print(f"\n\nSEQUENTIAL SEARCH COUNT: {seq_count}")
print(f"         BINARY SEARCH COUNT: {bin_count}")
 #boooo not found - alert your user!