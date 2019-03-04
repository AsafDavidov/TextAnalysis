#Programming assignment
#Asaf Davidov
#The first program will find the average word length of a Charles Dickens's A Tale of Two Cities
def averagewordlen():
    #first I opened the file
    inFile = open('A Tale of Two Cities.txt', 'r')

    allLines = inFile.readlines()

    allLinesstr = str(allLines)
    #used functions to find all the words
    allwords = allLinesstr.split()
    #used wordsum to create the average
    wordsum = 0
    #I used a for loop to add up all the words
    for word in allwords:
        wordlength = len(word)
        wordsum = wordlength + wordsum


    #This is for the calculation of the average length of the words.
    #I made sure a whole number because you cannot have a fraction of a word
    averageword_len = wordsum // len(allwords)
    print("The average length of each word in A Tale of Two Cities is:", averageword_len)


    #lastly i closed the file
    inFile.close()
averagewordlen()
