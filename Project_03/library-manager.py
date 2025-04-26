import streamlit as st
import json
import os

LIBRARY_FILE = 'library.json'

def load_library():
    if not os.path.exists(LIBRARY_FILE):
        return []
    with open(LIBRARY_FILE, 'r') as file:
        return json.load(file)

def save_library(library):
    with open(LIBRARY_FILE, 'w') as file:
        json.dump(library, file, indent=4)

def add_book(library, title, author, year):
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    save_library(library)
    st.success(f"✅ '{title}' added to your library!")

def view_books(library):
    if not library:
        st.info("📭 Your library is empty.")
    else:
        st.subheader("📚 Your Library:")
        for idx, book in enumerate(library, 1):
            st.write(f"{idx}. {book['title']} by {book['author']} ({book['year']})")

def search_book(library, query):
    found = [book for book in library if query.lower() in book['title'].lower()]
    if found:
        st.subheader("🔍 Search Results:")
        for book in found:
            st.write(f"{book['title']} by {book['author']} ({book['year']})")
    else:
        st.warning("🚫 No matching books found.")

def remove_book(library, title_to_remove):
    updated_library = [book for book in library if book['title'].lower() != title_to_remove.lower()]
    if len(updated_library) < len(library):
        save_library(updated_library)
        st.success(f"🗑️ '{title_to_remove}' removed from your library.")
    else:
        st.warning("🚫 Book not found.")

def main():
    st.title("📚 Personal Library Manager")
    library = load_library()

    menu = ["Add Book", "View All Books", "Search Book", "Remove Book"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Add Book":
        st.subheader("➕ Add a New Book")
        title = st.text_input("Enter Book Title")
        author = st.text_input("Enter Author Name")
        year = st.text_input("Enter Publication Year")
        if st.button("Add Book"):
            if title and author and year:
                add_book(library, title, author, year)
            else:
                st.warning("Please fill all fields.")

    elif choice == "View All Books":
        view_books(library)

    elif choice == "Search Book":
        st.subheader("🔍 Search for a Book")
        query = st.text_input("Enter title to search")
        if st.button("Search"):
            if query:
                search_book(library, query)
            else:
                st.warning("Please enter a search query.")

    elif choice == "Remove Book":
        st.subheader("🗑️ Remove a Book")
        title_to_remove = st.text_input("Enter title to remove")
        if st.button("Remove"):
            if title_to_remove:
                remove_book(library, title_to_remove)
            else:
                st.warning("Please enter a book title to remove.")

if __name__ == "__main__":
    main()
