
import streamlit as st
import json
import os

LIBRARY_FILE = 'library.json'

# Load existing library data or create a new file
def load_library():
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, 'r') as file:
        return json.load(file)

# Save current library data to the file
def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

# Add a new book
def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author name: ")
    year = input("Enter publication year: ")
    
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    save_library(library)
    print(f"✅ '{title}' added to your library!")

# View all books
def view_books(library):
    if not library:
        print("📭 Your library is empty.")
    else:
        print("\n📚 Your Library:")
        for idx, book in enumerate(library, 1):
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']})")

# Search for a book
def search_book(library):
    query = input("Enter title to search: ").lower()
    found = [book for book in library if query in book['title'].lower()]
    
    if found:
        print("\n🔍 Search Results:")
        for book in found:
            print(f"{book['title']} by {book['author']} ({book['year']})")
    else:
        print("🚫 No matching books found.")

# Remove a book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").lower()
    updated = [book for book in library if book['title'].lower() != title]
    
    if len(updated) < len(library):
        save_library(updated)
        print(f"🗑️ '{title}' removed from your library.")
    else:
        print("🚫 Book not found.")

# Main menu
def main():
    library = load_library()
    
    while True:
        print("\n=== Personal Library Manager ===")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_book(library)
        elif choice == '2':
            view_books(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            remove_book(library)
            library = load_library()  # reload after removal
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
# This code is a simple personal library manager that allows users to add, view, search, and remove books from their library.
# It uses a JSON file to store the library data persistently.