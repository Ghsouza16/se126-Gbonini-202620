# SE126 - Winter 2026
# Lab 7 - Dictionaries
# Programming Dictionary with Bubble Sort

import csv

# Load dictionary from file
def load_dictionary(filename):
    dictionary = {}

    try:
        with open(filename, "w7_lab.csv") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 2:
                    word = row[0]
                    definition = row[1]
                    dictionary[word] = definition
    except:
        print("File not found. Starting empty dictionary.")

    return dictionary


# Save dictionary to file
def save_dictionary(dictionary, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        for word in dictionary:
            writer.writerow([word, dictionary[word]])


# Show all words
def display_all(dictionary):

    if len(dictionary) == 0:
        print("Dictionary is empty")
        return

    for word in dictionary:
        print("\nWord:", word.upper())
        print("Definition:", dictionary[word])


# Bubble Sort function
def bubble_sort(words):

    n = len(words)

    for i in range(n):
        for j in range(0, n - i - 1):

            if words[j].lower() > words[j + 1].lower():
                temp = words[j]
                words[j] = words[j + 1]
                words[j + 1] = temp

    return words


# Show words alphabetically
def display_alphabetical(dictionary):

    if len(dictionary) == 0:
        print("Dictionary is empty")
        return

    words = list(dictionary.keys())

    bubble_sort(words)

    for word in words:
        print("\nWord:", word.upper())
        print("Definition:", dictionary[word])


# Search word
def search_word(dictionary):

    term = input("Enter word to search: ").lower()

    found = False

    for word in dictionary:

        if word.lower() == term:
            print("\nWord found:", word)
            print("Definition:", dictionary[word])
            found = True
            break

    if not found:
        print("Word not found")


# Add word
def add_word(dictionary):

    new_word = input("Enter new word: ")

    if new_word in dictionary:

        print("Word already exists")
        overwrite = input("Overwrite? (y/n): ")

        if overwrite.lower() == "y":
            definition = input("Enter new definition: ")
            dictionary[new_word] = definition

    else:
        definition = input("Enter definition: ")
        dictionary[new_word] = definition


# Main program
def main():

    dictionary = load_dictionary("words.csv")

    while True:

        print("\n--- PROGRAMMING DICTIONARY ---")
        print("1. Show all words")
        print("2. Search word")
        print("3. Add word")
        print("4. Show alphabetical (Bubble Sort)")
        print("5. Exit")

        choice = input("Choose: ")

        if choice == "1":
            display_all(dictionary)

        elif choice == "2":
            search_word(dictionary)

        elif choice == "3":
            add_word(dictionary)

        elif choice == "4":
            display_alphabetical(dictionary)

        elif choice == "5":
            save_dictionary(dictionary, "updated_words.csv")
            print("Dictionary saved. Goodbye.")
            break

        else:
            print("Invalid choice")


main()