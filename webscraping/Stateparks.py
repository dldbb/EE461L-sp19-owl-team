from bs4 import BeautifulSoup;
import requests;
import pandas as pd
url ="https://tpwd.texas.gov/spdest/parkinfo/maps/park_maps/"
url_response = requests.get(url)
soup=BeautifulSoup(url_response.content,"html.parser")
listdata=[]
data = soup.findAll("div",{"id": {"maincontent"}});
for info in data[0].findAll("ul"):
    listofwebsite=info.findAll("li")
    for website in listofwebsite:
        templist=[]
        templist.append(website.a.get_text())
        urlinner = "https://tpwd.texas.gov"+website.a['href']
        urlinnerresponse=requests.get(urlinner)
        soupinner = BeautifulSoup(urlinnerresponse.content,"html.parser")
        data1 = soupinner.find("div",{"class": {"latlong"}})
        for direction in data1.findAll("p"):
            templist.append(direction.get_text())
        listdata.append(templist)
dictionary ={
    "Name":[],
    "Latitude":[],
    "Longitude":[]
}
for lis in listdata:
    lis[0]="Name:"+lis[0]
    for entry in lis:
        ls = entry.split(':')
        key = ls[0]
        value = ls[1]
        dictionary[key].append(value)
df = pd.DataFrame(dictionary)
df.to_csv('./plant_csv_stateparks.csv')
print(listdata);