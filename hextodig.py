def hextodig(hexVal):
    hexVal = list(str(hexVal))
    nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    alphas = ('a', 'b', 'c', 'd', 'e', 'f')
    itr = len(hexVal)
    newVal = 0
    for i in hexVal:
        if i not in nums:
            for j in alphas:
                if i == j:
                    i = alphas.index(j) + 10
        i = int(i)
        newVal += i * 16 **(itr - 1)
        itr -= 1
    return newVal

def hextorgb(hexVal):
    itr = 0
    newList = []
    returnList = []
    for i in hexVal:
        if (itr+1) % 2 == 0:
            newList.append(hexVal[itr-1]+ hexVal[itr])
        itr += 1
    for i in newList:
        i = hextodig(i)
        returnList.append(i)
    return returnList
        

print(hextorgb('a81c13'))
