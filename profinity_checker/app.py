import urllib.request, urllib.parse, urllib.error

def read_text():
    quotes = open( "C:/Users/Hp/Desktop/repos/fullstack-nanodegree-miniprojects/profinity_checker/app.txt","r")
    content = quotes.read()
    print(content)
    check_profinity(content)
    quotes.close()
def check_profinity(text):
    text=text.replace("\n","+")
    text=text.replace(" ","+")
    connection = urllib.request.urlopen("http://www.purgomalum.com/service/containsprofanity?text="+text)
    output = connection.read()
    print(output)
    connection.close()

read_text()
