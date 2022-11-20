#Creates a borrow note.
import datetime
def borrowNote(list, name):
    date_time = datetime.datetime.now()
    B_file = open('borrow_notice.txt','w')
    B_file.write("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    B_file.write(name+"\n")
    B_file.write("-----------------NOTICE FOR BORROWING THE BOOK: \n\n")
   
    grand_Total = 0
    #Calculation of the grand total and writing the data onto the text B_file.
    for i in list:
        price = i[4].replace("$",'')
        price = float(price)
        B_file.write("Name of the book is: "+ i[1])
        B_file.write("Price of the book is: "+ i[4])
        
        grand_Total = grand_Total + price
    B_file.write("---------------------------------------\n")
    B_file.write("Grand Total:-\t\t\t$"+str(grand_Total)+"\n\n")
    B_file.write("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    B_file.write("The date you issued book is : " + str(date_time))
    B_file.close()


#Creates a return note.
def returnNote(list, days, name):
    date_time = datetime.datetime.now()
    R_file = open('return_notice.txt','w')
    total = 0
    R_file.write("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    R_file.write(name+"\n")
    R_file.write("--------------Notice For Returing the book------------------------------ \n\n")
    
    #Calculates the grand total after returning and fining and writes it to a text B_file.
    for i in list:
        fine = 0
        price = i[4].replace("$",'')
        price = float(price)
        fineDays = 0
        if days > 10:
            fineDays = days - 10
            fine = (1 / 0.6) * price * fineDays
        print("You are late in returing the book fine would up added")
        R_file.write("name of the book is: "+i[1])
        R_file.write("The price of the book is: "+i[4])
        R_file.write("The fine for this book is: "+str(fine)+"\n")
        
        total = total + price + fine
    R_file.write("---------------------------------------------------------------\n")
    R_file.write("Grand Total:-\t\t\t$"+str(total)+"\n\n")
    R_file.write("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+\n")
    R_file.write("The date you returned book is : " + str(date_time))
    R_file.close() 
