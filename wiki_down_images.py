import requests as r
from bs4 import BeautifulSoup as b

link = input('Enter the URL of the wikipedia page\n'.title())

rawdata = r.get(link).text

newdata = b(rawdata,'lxml')

img1 = newdata.findAll("img")

img2 = [i['src'] for i in img1] # all images links

def verify(s):                                          # bug fix. now only images in the list.
    temp = False
    if  str(s[2:22]) == 'upload.wikimedia.org':
        temp = True
    elif str(s[2:29]) == 'http://upload.wikimedia.org':
        temp = True
    elif str(s[2:30]) == 'https://upload.wikimedia.org':
        temp = True                                             
    return(temp)                                           

img1 = [str(i[2:]) for i in img2 if verify(i) == True]  


def add_http(s):
    if s[0:6] == 'upload':
        s = 'https://' + s 
    elif s[0:5] == 'http:':
        s = s[0:4] + 's' + s[4:]                    # standardizing the links. all links now have https://
    return(s)

def thumb_to_high_res(s):
    stop_string = ['svg','jpeg','jpg','gif','png','SVG','JPEG','JPG','GIF','PNG']
    for i in stop_string:               
        temp = s.find(i)                            
        if temp != -1:
            break
    if (s[temp:temp+3].lower() == 'jpe'):
        size = 4 
    else:                                       # this changes the link from the thumbnail address to the 
        size = 3                                # high res image link
    s = s[:temp + size]
    temp = s.find('/thumb')
    s = s[:temp] + s[temp + 6:]
    return(s)

img2 = [add_http(thumb_to_high_res(i)) for i in img1]

count = 1

for i in img2:
    permission = r.get(i)
    newfilename = i[52:]                        # downloads the images
    with open(newfilename,'wb') as p:
        p.write(permission.content)
    print(str(count) + '.\t' + newfilename + " Is Successful")
    count += 1