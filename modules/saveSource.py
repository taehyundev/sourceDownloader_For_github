import os
def saveFile(fileName, fileContents):
    URL = 'source/'+fileName
    print(URL)
    f = open(URL, mode='wt', encoding='utf-8')
    f.write(fileContents)
    f.close()