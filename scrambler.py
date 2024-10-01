import random
import sys

if sys.argv[1] == '-encrypt':
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
    with open(f'{sys.argv[2]}', 'r') as fileIn:
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
            with open(''.join(map(str, encNameList)) + '.txt', 'a') as scramFile:
                scramFile.write(' '.join(map(str, encrypted)))
                scramFile.write('\n')
            with open(''.join(map(str, keyNameList)) + '.txt', 'a') as keyFile:
                keyFile.write((' '.join(map(str, key))))
                keyFile.write('\n')

if sys.argv[1] == '-decrypt':
    scramFile = open(sys.argv[2])
    keyFile = open(sys.argv[3])
    for line in scramFile:
        decrypt = str(line)
        decryptList = decrypt.split()
        keyList = str(keyFile.readline())
        keyListList = map(int, keyList.split())
        keyWordPair = dict(zip(keyListList, decryptList))
        clearLine = ''
        for counter in range(0, len(keyWordPair)):
            clearLine = clearLine + ' ' + (keyWordPair.get(counter))
        print(clearLine)

if sys.argv[1] == '-help':
    print('Application for encrypting and decrypting text files.')
    print('Initial flags are -encrypt, -decrypt, and -help')
    print('-encrypt requires follow on argument of the target file, and an optional argument for a string name')
    print('example: python scrambler.py -encrypt simplestExample.txt "I love my wife all of the bunchies"')
    print('-decrypt requires follow on argument of target encrypted file, target key file, and optional argument of output name')
    print('example: python scrambler.py - decrypt Ilovemywife.txt allofthebunchies.txt decryptedtext.txt')