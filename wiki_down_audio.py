import requests as r
from bs4 import BeautifulSoup as b

link = input('Enter the URL of the wikipedia page\n'.title())

rawdata = r.get(link).text

newdata = b(rawdata,'lxml')

audio1 = newdata.findAll("source")

audio2 = [i['src'] for i in audio1] # all audio links

def verify(s):                                          # bug fix. now only audio files in the list.
    temp = False
    if  str(s[2:22]) == 'upload.wikimedia.org':
        temp = True
    elif str(s[2:29]) == 'http://upload.wikimedia.org':
        temp = True
    elif str(s[2:30]) == 'https://upload.wikimedia.org':
        temp = True                                             
    return(temp)                                           

audio1 = [str(i[2:]) for i in audio2 if verify(i) == True]  


def add_http(s):
    if s[0:6] == 'upload':
        s = 'https://' + s 
    elif s[0:5] == 'http:':
        s = s[0:4] + 's' + s[4:]                    # standardizing the links. all links now have https://
    return(s)

def get_add(s):
    stop_string = ['oga', 'mp3', 'wav', 'ogg']
    for i in stop_string:                                 
        temp = s.find(i)                           # this changes the link from the thumbnail address to the                     
        if temp != -1:                             # high res image link
            break                                
    s = s[:temp + 3]
    '''temp = s.find('/transcoded')
    if (temp != -1):
        s = s[:temp] + s[temp + 6:]'''
    return(s)

audio2 = [add_http(get_add(i)) for i in audio1]

count = 1

audio1 = [i for i in audio2 if i[-4:] == '.mp3'] # each music file has a ogg or wav format one too along with the mp3 file
                                                 # this downloads mp3 because it is the most widely used format
count = 1

def string_reverse(s):
    b = ''
    for i in s[len(s):0:-1]:
        b = b + i               # string reverse
    b = b + s[0]
    return(b)

def getfilename(s):
    b = string_reverse(s)
    loc = b.find('/')           # the string after the last \ in the link is the filename
    b = b[:loc]
    return(string_reverse(b))

for i in audio1:
    permission = r.get(i)
    newfilename = getfilename(i)                     # downloads the files
    with open(newfilename,'wb') as p:
        p.write(permission.content)
    print(str(count) + '.\t' + newfilename + " Is Successful")
    count += 1