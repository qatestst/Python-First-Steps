searched_book = input()
books_counter = 0

while True:
    new_book = input()
    if new_book == "No More Books":
        print(f"The book you search is not here!")
        print(f"You checked {books_counter} books.")
        break
    if new_book == searched_book:
        print(f"You checked {books_counter} books and found it.")
        break
    books_counter += 1


    # Example
    # searched_book = input("Enter the book you are searching for: ")
    # books_counter = 0
    # is_book_found = False
    #
    # new_book = input("Enter the next book: ")
    # while new_book != 'No More Books':
    #     if new_book == searched_book:
    #         is_book_found = True
    #         break
    #     books_counter += 1
    #     new_book = input("Enter the next book: ")
    #
    # if is_book_found:
    #     print(f"You checked {books_counter} books and found it.")
    # else:
    #     print(f"The book you search is not here!")
    #     print(f"You checked {books_counter} books.")


