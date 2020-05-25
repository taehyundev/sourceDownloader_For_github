from modules import getGitInfo
from urllib import parse
gitNickanme = input("What is your gitNickName >> ")
url = "http://github.com/"+gitNickanme

### getRepositories
repositInfo = getGitInfo.getRepositories(url)
extends = [".py", ".c"]

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
    if "py" in elementUrl:
        print("this is file")
        URL_S += "/" + parse.quote(elementUrl)
        source = getGitInfo.getSource(URL_S)
        break
    #else
    URL_S += "/" + parse.quote(elementUrl)
    elementInfo = getGitInfo.getElement(URL_S)


print(source)