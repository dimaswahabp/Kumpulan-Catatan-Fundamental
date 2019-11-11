
import math

def reverselist(theList) :
    for i in range(0, math.floor(len(theList)/2)):
        tempList = theList[i]
        theList[i] = theList[len(theList) - 1 - i]
        theList[len(theList) - 1 - i] = tempList
        
    return theList
print(reverselist(['andi','budi','caca','bambang','joko']))
