

f = open('Day4PassPhrases.txt','r')
message = f.read()

f.close()

lines = message.split("\n");

i = 0
i2 = 0


def sortWord(word):
    wordRA = list(word)
    wordRA.sort()
    # return "".join(wordRA)
    print (word)
    print (wordRA)
    return "".join(wordRA)


for line in lines:
    if len(line) == 0:
        next

    # print(str(i))
    lineIsGood = True;
    lineIsGood2 = True;


    words = line.split()

    wordCount = dict()
    wordCount2 = dict()
    if (len(words)== 0):
        lineIsGood = False
        lineIsGood2 = False
    else :
        for word in words:
            # print(word)

            # PHASE ONE:
            if word in wordCount:
                lineIsGood = False
                # print (line)
                # break;
            else:
                wordCount[word] = 1

            wordsorted = sortWord(word)
            if wordsorted in wordCount2:
                lineIsGood2 = False
            else:
                wordCount2[wordsorted] = 1


    if lineIsGood:
        # print ("'" + line + "'")
        i += 1

    if lineIsGood2:
        i2 += 1

print (str(i) + " valid passphrases")
print (str(i2) + " valid passphrases with anagrams")