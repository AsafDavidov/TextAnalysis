#Project Assignment 2
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
    print("The average length of each sentence in The Adventures of Huckleberry Finn is:", averageFsen, "words")
    print("The average length of each sentence in Pride and Prejudice is:", averagePsen, "words")
    print(" ")
    #last if statements comparing the two averages.
    if averageFsen > averagePsen:
        print("The average sentence length in The Adventures of Huckleberry Finn is longer by", averageFsen - averagePsen, "words.")
    else:
        print("The average sentence length in Pride and Prejudice is longer by", averagePsen - averageFsen, "words.")
    #closed the files
    inFinn.close()
    inPride.close()
#The last program will compare the number of times dialogue there is within two famous books. This will compare the style that each author used. 
#The two books are the Adventures of Sherlock Holmes by Arthur Conan Doyle and Siddartha by Herman Hesse.
def dialogue():
    #first open the files
    inHFile = open('Sherlock Holmes.txt', 'r')
    inSFile = open('Siddartha.txt', 'r')
    allHLines = inHFile.read()
    allSLines = inSFile.read()
    #split the words
    allHwords = allHLines.split()
    allSwords = allSLines.split()
    numHquotes = 0
    numSquotes = 0
    #To count the dialogue the first letter of a split word is gonna be a quotation
    for word in allHwords:
        if word[0] == '"':
            numHquotes = numHquotes + 1
    for word in allSwords:
        if word[0] == '"':
            numSquotes = numSquotes + 1


    print("The number of times there is dialogue in The Adventures of Sherlock Holmes is:", numHquotes)
    print("The number of times there is dialogue in Siddartha is:", numSquotes)
    print(" ")
    #This final if statement is to compare the amount of dialogue in each book.
    if numSquotes>numHquotes:
        print("Siddartha has", numSquotes-numHquotes, "more lines of dialogue than The Adventures of Sherlock Holmes.")
    else:
        print("The Adventures of Sherlock Holmes has", numHquotes-numSquotes, "more lines of dialogue than Siddartha.")
    #lastly I closed the file

    inHFile.close()
    inSFile.close()
def main():
    books = input("Type A to find the average word length in A Tale of Two Cities. Type B to compare the sentence length between The Adventures of Huckleberry Finn and Pride and Prejudice. Lastly, Type C to find out which book has more dialogue; Siddartha or The Adventures of Sherlock Holmes: ").lower()
    if books == "a":
        averagewordlen()
    elif books == "b":
        avgsen()
    elif books == "c":
        dialogue()
main()
    
