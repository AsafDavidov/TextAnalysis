#Asaf Davidov
#part b
#The last program will compare the number of times dialogue there is within two famous books. This will compare the style that each author used. 
#The two books are the Adventures of Sherlock Holmes by Arthur Conan Doyle and Siddartha by Herman Hesse.
#2/18/2013
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
    print(" ")
    print("The number of times there is dialogue in Siddartha is:", numSquotes)
    print(" ")
    #This final if statement is to compare the amount of dialogue in each book.
    if numSquotes>numHquotes:
        print("Siddartha has dialogue", numSquotes-numHquotes, "more times than The Adventures of Sherlock Holmes.")
    else:
        print("The Adventures of Sherlock Holmes has dialogue", numHquotes-numSquotes, "more times than Siddartha.")
    #lastly I closed the file

    inHFile.close()
    inSFile.close()
dialogue()
