def createChoices(x, z):
    num = 1
    for y in x:
        print("{}) {}".format(num, y))
        num +=1
        
    inp = input('Your Selection: ')
    z.append(x[int(inp)-1])

def listToString(x):
    str1 = " "
    return (str1.join(x))

def getSubList(x, character):
    choiceArr = []
    newArr = []
    for a in x:
        if len(a) > 1:
            charInd = x.index(a)
            choiceArr = a
            print("{} in {} has multiple pronounciations. Type the number of the one you want.".format(character[charInd], character))
            createChoices(choiceArr, newArr)
        elif len(a) == 1:
            for y in a:
                newArr.append(y)
    
    return(listToString(newArr))
