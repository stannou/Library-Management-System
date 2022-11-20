#Main file of the code.
#importing functions from different modules.
import loadingList
import functions
import noteGenerator
import listManipulation
#Saves the imported list as list2.
list2 = loadingList.load('Books.txt','r')
# userName = input("Enter your full name.: ")
#Setting up variables
cart = []
returned = []
daysBorrowed = 0
z = 1
#Creating infinite loop which breaks when user input is 4.
while z>0:
    #Calling function menu from functions module.
    functions.menu()
    choice = input("Enter your choice: ")
    try:
        if choice == "D":
        # #Calling function menu1 from functions module.
        # functions.menu1(list2)
            file = open("Books.txt","r")
            text = file.read()
            print(text)
        elif choice == "L":
           
            #Calling function menu2 from functions module.
            Id = functions.menu2(list2)
            userName = input("Enter your full name.: ")
            for i in list2:
                if Id == i[0]:
                    if int(i[3])>0:
                        #Adding the file to cart and reducing the stock.
                        cart.append(i)
                        stock = int(i[3])
                        stock = stock - 1
                        i[3] = str(stock)
                    else:
                        print("\n----------------------------Sorry the item is out of stock.--------------------------------\n")
                
                    
        elif choice == "R":
        #Calling function menu3 from functions module.
            userName = input("Enter you name: ")
            Id = functions.menu3(list2)  
            daysBorrowed =  int(input("\nEnter the number of days you have had the book for: "))
            for i in list2:
                if Id == i[0]:
                #Adding the file to returned list and increasing the stock.
                    returned.append(i)
                    stock = int(i[3])
                    stock = stock + 1
                    i[3] = str(stock)
                
                    
           
        elif choice == "Q":
            print("------------Thanks for visiting our Libary Keep coming----------------")
            break
        else:
            print("\n----------------------Enter a valid Choice.--------------------\n")
    except Exception as e:
        print(e)
#Creating a borrow note from noteGenerator module. 
noteGenerator.returnNote(returned, daysBorrowed, userName)
#Creating a return note from noteGenerator module.
noteGenerator.borrowNote(cart, userName)
#Appending the list by calling appendList function from listManipulation module and manipulating the stock of the books
listManipulation.appendList(list2)
