import random
import sys

fileIn = open(f'{sys.argv[1]}', 'r')
lineNum = 0
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
    print(f'line processed: {lineNum}')
    lineNum += 1




