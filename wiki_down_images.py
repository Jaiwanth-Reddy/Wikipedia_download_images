from bs4 import BeautifulSoup as b
import requests as r

link = input("Enter the Wikipedia page URL\n".title())

permission = r.get(link).text

rawdata = str(b(permission,'lxml'))

with open('txt_of_html_first.txt','w',encoding='utf-8',errors='ignore') as p:
    p.write(rawdata)


link = 'txt_of_html_first.txt'

with open(link,'r',encoding='utf-8',errors='ignore') as p:
    rawdata = p.read()

biglist = []

start = 'upload.wikimedia.org/wikipedia/commons/thumb/'
end = '.png'

while 1:
    a = rawdata.find(start)
    b = rawdata[a:].find(end)
    temp = rawdata[a:b+a]
    biglist.append(temp)
    rawdata = rawdata[a+b:]
    if (a == -1):
        break

biglist = list(set(biglist))
biglist = sorted(biglist)


with open('biglist.txt','w',encoding='utf-8',errors='ignore') as p:
    for i in biglist:
        p.write(i + '\n')

link = 'biglist.txt'
final_list = []

with open(link,'r',encoding='utf-8',errors='ignore') as p:
    biglist = p.readlines()

for item in biglist:
    start = item.find('.svg')
    item = item[:start+4]
    start = item.find('thumb')
    s1 = item[:start]
    s2 = item[start+6:]
    s1 = s1 + s2
    final_list.append(s1)
    
final_list = [i for i in final_list if i != '']
final_list = ['http://' + i for i in final_list]
final_list = list(set(final_list))

for i in final_list:
    permission = r.get(i)
    newfilename = i[51:]
    with open(newfilename,'wb') as p:
        p.write(permission.content)
    print(newfilename + " Is Successful")
