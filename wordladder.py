# Moinak Das

#open txt file of all words, save as list
f = open("C:/classwork/dictall.txt","r")
wordlist = f.read().split()

#
def wordladder(start, end):
    """Assumes start and end are strings in dictall.txt
       returns wordladder between start and end (list)"""
    #currentList
    currentList = []
    currentList.append(start)

    #filter wordlist by word length
    wList = filterList(len(start), wordlist)

    #while the last item in the currentList is not the word we're looking for
    while(currentList[-1] != end):
        #create a dictionary where the key is a word, and its value is the "distamce" to
        #the end word
        OneFromStart = {}
        for i in range(len(wList)):
            if(calculateDistance(currentList[-1], wList[i]) == 1):
                OneFromStart[wList[i]] = calculateDistance(wList[i],end)
        #sort dictionary by value, so the words closer to the end word are prioritized
        OneFromStart = sortDictionary(OneFromStart)

        #if the list is not empty
        if(len(OneFromStart) > 0):
            #add the closet word (first key in the dictionary) to the currentList
            currentList.append(list(OneFromStart.keys())[0])
            #remove it from our masterList of words so it can't repeat
            wList.remove(list(OneFromStart.keys())[0])
        else:
            #otherwise, we go back to the previous word
            currentList.remove(currentList[-1])

    print(currentList)
    return currentList

    
def filterList(length, listof):
    """Assumes length is an integer, listof is a list
       Removes any item from listof that is not length length
       and returns list"""
    newlist = []
    for i in range(len(listof)):
        if(len(listof[i]) == length):
            newlist.append(listof[i])
    return newlist

def calculateDistance(start,end):
    """calculates how many letters are different
       between start and end"""
    if(len(start) == len(end)):
        counter = 0
        for i in range(len(start)):
            if(start[i] != end[i]):
                counter += 1
        return counter
    else:
        raise Exception("start and end must have the same length")

def sortDictionary(x):
    """x is a dictionary, sorts dictionary by value"""
    return dict(sorted(x.items(), key=lambda item: item[1])) #had help for this particular line of code (stack overflow)


wordladder("hate","love")