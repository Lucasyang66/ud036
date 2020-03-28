import urllib.request

def read_text ():
    text=open ("C:\\Users\\lucas\\Desktop\\ud036\\Famous_Movie_Quotes.txt")
    contents_of_file=text.read()
    text.close()    
    print("contents_of_file ",contents_of_file)
    new_contents_of_file=contents_of_file.split('\n')
    print('new_contents_of_file ',new_contents_of_file)
    for x in new_contents_of_file:     
        check_curse(x)
def check_curse(text):
    connection=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+text)
    output=connection.read()
    connection.close()
    #print(output)
    if  'true' in str(output) :
       print(text," the curse word is in the document")
    else:
      print(text," no cuse word")

read_text()
