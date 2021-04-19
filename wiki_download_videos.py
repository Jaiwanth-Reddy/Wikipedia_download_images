import requests as r
from bs4 import BeautifulSoup as b

link = input("Enter the link\n".title())

perm = r.get(link).text

rawdata = b(perm,'lxml')

#video1 = rawdata.findAll("video",{"src":True})

video1 = rawdata.findAll("video")
video3=[]

for j in range(0,len(video1)):
    video2 = [i['src'] for i in video1[j]]  # all the videos that dont have a 'click to play' button are added 
    video3.append(video2[0])                # to the downloads list


video1 = rawdata.findAll("div")

video2 = [str(i) for i in video1]

temp = []

for i in video2:
    start = i.find("src=")
    end = i[start + 5:].find('"')           # all other videos are in div tag. using src = , those links are added
    if start != -1:
        temp.append(i[start:end + start + 5])


for i in range(0,len(temp),3):              # each video has three links of varying resolutions. highest res is
    if temp[i][-4:] == 'webm':              # downloaded
        video3.append(temp[i][5:])

def add_http(s):
    s = 'https:' + s                    # standardizing the links. all links now have https://
    return(s)

video2 = [add_http(i) for i in video3]
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


count = 1

for i in video2:
    permission = r.get(i)
    newfilename = getfilename(i)                     # downloads the files
    with open(newfilename,'wb') as p:
        p.write(permission.content)
    print(str(count) + '.\t' + newfilename + " Is Successful")
    count += 1