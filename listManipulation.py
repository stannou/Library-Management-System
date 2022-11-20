#Rewrites the initial text file with the new data gained through the user interactions.
def appendList(list):
    file = open('Books.txt','w')
    for i in list:
        for j in range(len(i)):
            file.write(i[j])
            if j < 4:
                file.write(",")
        file.write('\n')

