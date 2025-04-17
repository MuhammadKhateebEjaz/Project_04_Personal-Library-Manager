import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
         with open(data_file, 'r') as file:
              return json.load(file)
         return []
    
    def save_library(library):
         with open(data_file, file):
              json.dump(library, file)

      def add_book(library):
         title = input('Enter the title of the book: ')  
    author = input('Enter the author of the book: ')
    year = input('Enter the year of the book: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have You Read the book? (yes/no): ').lower() == "yes"

new_book = {
     'title' : title,
     'author' : author,
      'year'  : year,
      'genre' : genre,
      'read'  : read,

}


library.append(new_book)
save_library(library)
print(f'Book {title} addes successfully'.)









