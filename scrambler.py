import random
import sys

if sys.argv[1] == '-encrypt':
    fileIn = open(f'{sys.argv[2]}', 'r')
    if len(sys.argv) > 3:
        nameIn = f'{sys.argv[3]}'
    else:
        nameIn = 'encrypted keys'

    outNameList = nameIn.split()
    encNameList = []
    for each in range(0, (len(outNameList) // 2)):
        encNameList.append(outNameList[each])   
    for each in encNameList:
        outNameList.remove(each)
    keyNameList = outNameList

    for line in fileIn:
        strIn = line
        userIn = strIn.split()
        keyList = userIn.copy()
        encrypted = []
        key = []
        while len(userIn) != 0:
            remDex = random.randint(0, len(userIn) - 1)
            remWord = userIn.pop(remDex)
            encrypted.append(remWord)
            key.append(keyList.index(remWord))
        with open(' '.join(map(str, encNameList)) + '.txt', 'a') as scramFile:
            scramFile.write(' '.join(map(str, encrypted)))
            scramFile.write('\n')
        with open(' '.join(map(str, keyNameList)) + '.txt', 'a') as keyFile:
            keyFile.write((' '.join(map(str, key))))
            keyFile.write('\n')

    fileIn.close()
    scramFile.close()
    keyFile.close()


