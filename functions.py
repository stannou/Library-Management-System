#Displays a menu which makes it easy for the user to carry out a function.
def menu():
    print("Press D to display the book")
    print("Press L to lend the book")
    print("Press R to Return the book")
    print("Press Q to Quit the Program")

#Displays the name of book and the price.
def menu1(list):
    print("\n\nBook Name\t\t\tPrice")
    for i in list:
        print(i[1]+"\t\t\t"+i[4])

#Displays the Book ID, the name of the book and the price of the book.
#Asks for the book ID.
def menu2(list):
    print("\nBook ID\t\tBook Name\t\t\tPrice")
    for i in list:
        print(i[0]+"\t\t"+i[1]+"\t\t\t"+i[4])
    bookId = input("\nEnter the book id of the book you choose to borrow: ")
    return bookId    

#Displays the Book ID, the name of the book and the price of the book.
#Asks for the book ID.
def menu3(list):
    print("\nBook ID\t\tBook Name\t\t\tPrice")
    for i in list:
        print(i[0]+"\t\t"+i[1]+"\t\t\t"+i[4])
    bookId = input("\nEnter the book id of the book you choose to return: ")
    return bookId




