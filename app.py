from modules import getGitInfo
from modules import saveSource
from urllib import parse

gitNickanme = input("What is your gitNickName >> ")
url = "http://github.com/"+gitNickanme

### 확장자
extends = ['.py', '.c', '.cpp', '.java','.md','.cs']
fileName =str()

### getRepositories
repositInfo = getGitInfo.getRepositories(url)

# repositInfo print
for i in range(len(repositInfo)):
    print(str(i+1)+ " : "+repositInfo[i])
selectReposit =int(input(">> "))

# repositUrl 
repositUrl = repositInfo[selectReposit-1]
elementInfo = getGitInfo.getElement(url+"/"+repositUrl)

URL_S = url+"/"+repositUrl + "/tree/master"
while(True):

    # elementprint
    for i in range(len(elementInfo)):
        print(str(i+1)+ " : "+elementInfo[i])
    selectReposit =int(input(">> "))
    elementUrl = elementInfo[i-1]
    print(elementUrl)
    #extends에 따라 파일이 select 되면 바로 파일 출력
    isfile = False
    for i in range(len(extends)):
        if extends[i] in elementUrl:
            print("this is file")
            fileName = elementUrl
            URL_S += "/" + parse.quote(elementUrl)
            source = getGitInfo.getSource(URL_S)
            isfile =True
            break
    if isfile == True:
        break
    #else
    URL_S += "/" + parse.quote(elementUrl)
    elementInfo = getGitInfo.getElement(URL_S)


print(source)

is_saveFile = input("파일을 저장하시겠습니까?(Y/N) >>" )

if is_saveFile == 'Y'or is_saveFile == 'y':
    saveSource.saveFile(fileName,source)