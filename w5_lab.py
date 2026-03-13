import csv

def read_file(filename):
    """Reads the CSV file and stores data in parallel lists"""
    numbers = []
    titles = []
    authors = []
    genres = []
    pages = []
    status = []
    
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) >= 6:
                numbers.append(row[0])
                titles.append(row[1])
                authors.append(row[2])
                genres.append(row[3])
                pages.append(row[4])
                status.append(row[5].lower())
    
    return numbers, titles, authors, genres, pages, status

def show_book(index, numbers, titles, authors, genres, pages, status):
    """Shows a single book"""
    print(f"#: {numbers[index]} | Title: {titles[index]} | Author: {authors[index]} | "
          f"Genre: {genres[index]} | Pages: {pages[index]} | Status: {status[index].capitalize()}")

def show_all(numbers, titles, authors, genres, pages, status):
    """Shows all books"""
    print("\n" + "="*100)
    for i in range(len(titles)):
        show_book(i, numbers, titles, authors, genres, pages, status)
    print("="*100)

def show_sorted(numbers, titles, authors, genres, pages, status):
    """Shows all books sorted by title (BONUS)"""
    # Create list of indices sorted by title
    indices = list(range(len(titles)))
    for i in range(len(indices)-1):
        for j in range(len(indices)-i-1):
            if titles[indices[j]].lower() > titles[indices[j+1]].lower():
                indices[j], indices[j+1] = indices[j+1], indices[j]
    
    print("\n" + "="*100)
    print("BOOKS SORTED BY TITLE:")
    for idx in indices:
        show_book(idx, numbers, titles, authors, genres, pages, status)
    print("="*100)

def sequential_search(list_to_search, term):
    """Sequential search - returns list of found indices"""
    term = term.lower()
    found = []
    for i in range(len(list_to_search)):
        if term in list_to_search[i].lower():
            found.append(i)
    return found

def binary_search(list_to_search, target):
    """Binary search - returns index or -1 if not found"""
    # Create pairs (value, original index) and sort
    pairs = [(list_to_search[i], i) for i in range(len(list_to_search))]
    for i in range(len(pairs)-1):
        for j in range(len(pairs)-i-1):
            if pairs[j][0] > pairs[j+1][0]:
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
    
    # Extract sorted values and original indices
    sorted_values = [p[0] for p in pairs]
    original_indices = [p[1] for p in pairs]
    
    # Binary search
    start = 0
    end = len(sorted_values) - 1
    
    while start <= end:
        middle = (start + end) // 2
        if sorted_values[middle] == target:
            return original_indices[middle]
        elif sorted_values[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
    
    return -1

def menu():
    """Shows the main menu"""
    print("\n" + "="*40)
    print("     PERSONAL LIBRARY SYSTEM")
    print("="*40)
    print("1. Show All Titles")
    print("2. Search by Title")
    print("3. Search by Author")
    print("4. Search by Genre")
    print("5. Search by Library Number")
    print("6. Show Available")
    print("7. Show On Loan")
    print("8. EXIT")
    print("="*40)

def main():
    # Load data
    numbers, titles, authors, genres, pages, status = read_file('book_list.csv')
    
    while True:
        menu()
        option = input("Choose an option (1-8): ")
        
        if option == '1':
            bonus = input("Show sorted by title? (y/n): ").lower()
            if bonus == 'y':
                show_sorted(numbers, titles, authors, genres, pages, status)
            else:
                show_all(numbers, titles, authors, genres, pages, status)
        
        elif option == '2':
            term = input("Enter title or keyword: ")
            indices = sequential_search(titles, term)
            if indices:
                print(f"\nFound {len(indices)} book(s):")
                for i in indices:
                    show_book(i, numbers, titles, authors, genres, pages, status)
            else:
                print("No books found.")
        
        elif option == '3':
            term = input("Enter author name: ")
            indices = sequential_search(authors, term)
            if indices:
                print(f"\nFound {len(indices)} book(s):")
                for i in indices:
                    show_book(i, numbers, titles, authors, genres, pages, status)
            else:
                print("No books found.")
        
        elif option == '4':
            term = input("Enter genre: ")
            indices = sequential_search(genres, term)
            if indices:
                print(f"\nFound {len(indices)} book(s):")
                for i in indices:
                    show_book(i, numbers, titles, authors, genres, pages, status)
            else:
                print("No books found.")
        
        elif option == '5':
            term = input("Enter library number: ")
            index = binary_search(numbers, term)
            if index != -1:
                print("\nBook found:")
                show_book(index, numbers, titles, authors, genres, pages, status)
            else:
                print("Library number not found.")
        
        elif option == '6':
            indices = sequential_search(status, "available")
            if indices:
                print(f"\n{len(indices)} available book(s):")
                for i in indices:
                    show_book(i, numbers, titles, authors, genres, pages, status)
            else:
                print("No available books.")
        
        elif option == '7':
            indices = sequential_search(status, "on loan")
            if indices:
                print(f"\n{len(indices)} book(s) on loan:")
                for i in indices:
                    show_book(i, numbers, titles, authors, genres, pages, status)
            else:
                print("No books on loan.")
        
        elif option == '8':
            print("Exiting program... Goodbye!")
            break
        
        else:
            print("Invalid option! Try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()