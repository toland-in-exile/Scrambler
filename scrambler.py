import random

fileIn = open('testViaDebug.txt', 'r')

for line in fileIn:
    strIn = fileIn.readline()
    userIn = strIn.split()
    keyList = userIn.copy()
    encrypted = []
    key = []
    while len(userIn) != 0:
        remDex = random.randint(0, len(userIn) - 1)
        remWord = userIn.pop(remDex)
        encrypted.append(remWord)
        key.append(keyList.index(remWord))
        print(' '.join(map(str, encrypted)))
        print(' '.join(map(str, key)))




