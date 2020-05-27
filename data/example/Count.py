import pandas as pd

lines=0
wordCount=0
file = open('/home/kaoun/pep/data/example/train.words.txt',newline='')
labeledData = pd.read_excel('/home/kaoun/Bureau/labeledData.xlsx')
i=0


for lineOfText in file:
    seq = ''
    lines += 1
    f1=lineOfText.split()

    wordCount = wordCount + len(f1)
    for index in range (i, wordCount ):
      seq = seq + ' '+ str(labeledData['Labels'][index])
    with open('/home/kaoun/pep/data/example/train.tags.txt','a') as file:
      file.write(seq +'\n')


    i = wordCount
    print(i)
