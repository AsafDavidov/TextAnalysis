#Asaf Davidov
#part C
#The second program will compare the sentence length of two famous books.
#The books are The Adventures of Huckleberry Finn by Mark Twain and Pride and Prejudice by Jane Austen
def avgsen():
    #First I opened the two famous books as text files.
    inFinn = open('The Adventures of Huckleberry Finn.txt', 'r')
    inPride = open('Pride and Prejudice.txt', 'r')
    #Then read the contents
    allFContents = inFinn.read()
    allPContents = inPride.read()
    #Then split the contents
    allFwords = allFContents.split()
    allPwords = allPContents.split()
    #found total number of words in the file
    totalFwords = len(allFwords)
    totalPwords = len(allPwords)
    #setup so I could find total number of sentences
    numFsen = 0
    numPsen = 0
    
    for word in allFwords:
        #This is how to find the total number of sentences while including all types of punctuation
         if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            numFsen = numFsen +1

    for word in allPwords:
        #Repeated the process for Pride and Prejudice
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            numPsen = numPsen + 1

    #Calculations for averages
    averageFsen = totalFwords//numFsen
    averagePsen = totalPwords//numPsen

    #last if statements comparing the two averages.
    if averageFsen > averagePsen:
        print("The average sentence length in The Adventures of Huckleberry Finn is longer by", averageFsen - averagePsen, "words.")
    else:
        print("The average sentence length in Siddartha is longer by", averagePsen - averageFsen, "words.")
    #closed the files
    inFinn.close()
    inPride.close()

avgsen()
    
