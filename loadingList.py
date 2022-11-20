#Loads the data from the text file.
def load(filename, mode):
    file1= open(filename, mode)
    contents= file1.read()
    file1.close()
    #Splits the list in places where lines separate.
    list1= contents.split('\n')
    list2=[]
    for each_item in list1:
        #Splits the list where there is a comma.
        list2.append(each_item.split(","))
    #Since the last element of the text file is an empty space it gets removed. 
    list2.pop()
    return list2


