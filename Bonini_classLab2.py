#W2 in class lab
#PROGRAM PROMPT:

#VARIABLE DICTIONARY:


#--IMPORTS-------------------------------------------
import csv


# FUNCTIONS -------------------------------------------
def difference(people: int, max_cap: int) -> int:
    """Return how many seats remain (positive) or how many over capacity (negative).

    Args:
        people: current number of people in the room
        max_cap: maximum capacity of the room

    Returns:
        max_cap - people
    """
    return max_cap - people


def main() -> None:
    # initialize counters
    total_records = 0    # total records in file (1 room per record)
    rooms_over = 0       # total number of rooms over capacity

    print(f"{'ROOM NAME':20} {'MAX':5} {'PPL':5} {'REMOVE':6}")
    print("-" * 50)

    csv_path = "classLab2 (1).csv"

    # read CSV and process
    try:
        with open(csv_path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for record in reader:
                # skip short/empty lines
                if len(record) < 3:
                    continue

                name = record[0].strip()
                # try to parse numeric fields; skip header or malformed rows
                try:
                    max_cap = int(record[1])
                    ppl = int(record[2])
                except ValueError:
                    # likely a header row or bad data; skip
                    continue

                total_records += 1

                remaining = difference(ppl, max_cap)
                if remaining < 0:
                    rooms_over += 1
                    # print how many people must be removed (-remaining)
                    print(f"{name:20} {max_cap:5} {ppl:5} {-remaining:6}")

    except FileNotFoundError:
        print(f"Error: file not found: {csv_path}")
        return

    print("-" * 50)
    # display final values: total rooms counted and number over capacity
    print(f"\n\nROOMS OVER CAPACITY: {rooms_over}\nTOTAL ROOMS in FILE: {total_records}")


if __name__ == "__main__":
    main()