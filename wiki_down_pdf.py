# not much original code here, just to make a final set 

import requests as r

link = input("Enter Wikipedia URL\n")

down_link = 'api/rest_v1/page/pdf'

t = link.find('wiki/')

newfilename = link[30:] + '.pdf'
link = link[:t] + down_link + link[t + 4:]      # getting the pdf link from the article link

permission = r.get(link)                    # downloads the files
with open(newfilename,'wb') as p:
    p.write(permission.content)
print(newfilename + " Is Successful")
