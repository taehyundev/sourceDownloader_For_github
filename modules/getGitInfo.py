from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib import parse

# repositories
def getRepositories(url):
    url += "?tab=repositories"
    repositInfo = list()
    with urlopen(url) as response:
        contents = BeautifulSoup(response, 'html.parser')
        for anchor in contents.find_all(class_='wb-break-all'):
            name = anchor.get_text()
            name = name.replace(' ','')
            name = name.replace('\n','')
            repositInfo.append(name)
    return repositInfo

# element
def getElement(url):
    elementInfo = list()
    with urlopen(url) as response:
        contents = BeautifulSoup(response, 'html.parser')
        for anchor in contents.find_all(class_='js-navigation-open'):
            if anchor.get('title') != None and anchor.get('title') != 'Go to parent directory':
                elementInfo.append(anchor.get('title'))

    return elementInfo

# source
def getSource(url):
    print("<source file>\n\n")
    source = str()
    with urlopen(url) as response:
        contents = BeautifulSoup(response, 'html.parser')
        for anchor in contents.find_all(class_='blob-code blob-code-inner js-file-line'):
            source = source + anchor.get_text() +'\n'
    return source