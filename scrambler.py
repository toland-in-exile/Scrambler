import random
import sys

lineNum = 0

fileIn = open(f'{sys.argv[1]}', 'r')
if len(sys.argv) > 2:
    nameIn = {sys.argv[2]}
else:
    nameIn = 'encrypted keys'

outNameList = nameIn.split()
encNameList = []
for each in range(0, (len(outNameList) // 2)):
    encNameList.append(each)
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
    with open(f'{' '.join(map(str, encNameList))}', 'a') as scramFile:
        scramFile.write(' '.join(map(str, encrypted)))
        scramFile.write('\n')
    with open(' '.join(map(str, keyNameList)), 'a') as keyFile:
        keyFile.write((' '.join(map(str, key))))
        keyFile.write('\n')
    print(f'line processed: {lineNum}')
    lineNum += 1


fileIn.close()
scramFile.close()
keyFile.close()


