import urllib.request

def read_text ():
    text=open ("C:\\Users\\lucas\\Desktop\\ud036\\Famous_Movie_Quotes.txt")
    contents_of_file=text.read()
    text.close()
    check_curse(contents_of_file)
def check_curse(text):
    print(text)
    connection=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=connection.read()
    connection.close()
    if  output :
       print("the curse word is in the document")
    else:
      print("no cuse word")

read_text()
