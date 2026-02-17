# Week 3 demo - corrected version of w3_Introlist.py

import csv
import datetime


def main() -> None:
    print("\n\tWelcome to lab #2 - Machine info Display")

    total_records = 0

    # parallel lists for each field
    machine_type = []
    brand = []
    proc = []
    ram = []
    first_hd = []
    num_hd = []
    second_hd = []
    os_list = []
    yr = []

    print(f"{'TYPE':10}{'BRAND':12}{'PROC':8}{'RAM':6}{'1st HD':8}{'2nd HD':8}{'OS':8}{'YEAR':6}")
    print("-" * 90)

    # file in repo: change path if your CSV is elsewhere
    csv_path = r"filehandling.csv"

    current_year = datetime.date.today().year
    age_threshold = 10

    try:
        with open(csv_path, newline='') as f:
            reader = csv.reader(f)
            for rec in reader:
                # skip empty rows and probable header rows
                if not rec:
                    continue
                if len(rec) < 9:
                    # skip short/malformed or header rows
                    continue

                # Type
                t = rec[0].strip().upper()
                if t == 'D':
                    machine_type.append('Desktop')
                elif t == 'L':
                    machine_type.append('Laptop')
                else:
                    machine_type.append('ERROR')

                # Brand
                b = rec[1].strip().upper()
                brand_map = {'DL': 'DELL', 'GW': 'Gateway', 'HP': 'HP'}
                brand.append(brand_map.get(b, 'ERROR'))

                proc.append(rec[2].strip())
                ram.append(rec[3].strip())
                first_hd.append(rec[4].strip())
                num_hd.append(rec[5].strip())
                second_hd.append(rec[6].strip())
                os_list.append(rec[7].strip())
                yr.append(rec[8].strip())

                total_records += 1

    except FileNotFoundError:
        print(f"Error: CSV file not found at: {csv_path}")
        return

    # Print table
    for i in range(total_records):
        print(f"{machine_type[i]:10}{brand[i]:12}{proc[i]:8}{ram[i]:6}{first_hd[i]:8}{num_hd[i]:8}{second_hd[i]:8}{os_list[i]:8}{yr[i]:6}")

    print("-" * 90)

    # Count old machines (>= age_threshold years)
    old_desktops = 0
    old_laptops = 0

    for i in range(total_records):
        try:
            manufacture_year = int(yr[i])
        except ValueError:
            # skip invalid year entries
            continue

        age = current_year - manufacture_year
        if age >= age_threshold:
            t = machine_type[i].lower()
            if t.startswith('desktop'):
                old_desktops += 1
            elif t.startswith('laptop'):
                old_laptops += 1
            else:
                print(f"Error: unknown machine type at index {i}")

    print("\nMachines processed for replacement budget:")
    print(f"Desktops to replace: {old_desktops} @ $2,000 each --> $ {old_desktops * 2000:,.2f}")
    print(f"Laptops to replace:  {old_laptops} @ $1,500 each --> $ {old_laptops * 1500:,.2f}")

    total_cost = (old_desktops * 2000) + (old_laptops * 1500)
    print(f"\n\tTotal replacement Cost: ${total_cost:,.2f}")

    print(f"\nTOTAL RECORDS: {total_records}\n\nThank you for using my program. Goodbye!\n")


if __name__ == '__main__':
    main()
