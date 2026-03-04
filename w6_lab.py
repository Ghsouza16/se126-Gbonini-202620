
#7 ROWS: 1  7
#4 seat types: A, B, C, D

seatA= ['A', 'A', 'A', 'A', 'A', 'A', 'A']
seatB= ['B', 'B', 'B', 'B', 'B', 'B', 'B']
seatC= ['C', 'C', 'C', 'C', 'C', 'C', 'C']
seatD= ['D', 'D', 'D', 'D', 'D', 'D', 'D']

#print the seat map!
for i in range(0, 7):
    print(f"{i+1}  {seatA[i]}  {seatB[i]}  {seatC[i]}    {seatD[i]}")

#ask the user for ROW: 1-7
row = int(input("Enter your desired ROW [1-7]:"))

#ask user for SEAT: A, B, C ,D
seat = input("Enter yur deisred SEAT [A/B/C/D]")

#check seat and replace with X to reserve, alert user if not
if seat == 'A': #seatA list
    if seatA[row -1] != "X":
        seatA[row -1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken,")
elif seat == 'B': #seatA list

if seat == 'A': #seatA list
    if seatA[row -1] != "X":
        seatA[row -1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken,")
elif seat == 'B': #seatA list

if seat == 'A': #seatA list
    if seatA[row -1] != "X":
        seatA[row -1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken,")
elif seat == 'B': #seatA list


if seat == 'A': #seatA list
    if seatA[row -1] != "X":
        seatA[row -1] = "X"
    else:
        print(f"Sorry, seat {row}{seat} is already taken,")
elif seat == 'B': #seatA list


