import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import math

#make python request to get content from webpage

r=requests.get("https://nigeriapropertycentre.com/for-rent?keywords=yaba&page=1")
c=r.content

print(c)

#parse content to html parser to convert html document to python data type
soup=BeautifulSoup(c,"html.parser")
real=soup.find_all("div",{"class":"wp-block-footer"}) #find all div classes 
print(real)
#grab a text from one of the div classes 
print(real[0].get_text().strip())
#extract keyword with regular expressions from text
print(re.findall("..Bathrooms",real[0].get_text().strip()))
card_n = soup.find_all("div", {"class":"col-sm-8 col-xs-12"})[0].text.strip().split(" ")[3]
print(card_n)
card_t = soup.find_all("div", {"class":"col-sm-8 col-xs-12"})[0].text.strip().split(" ")[5]
print(card_t)

num_pages = math.ceil(int(card_t)/int(card_n))
print("Number of Pages: ",num_pages)

locations = ["yaba", "ogba", "iyana+ipaja", "surulere", "gbagada", "ikeja", "lekki", "ajah", "ikorodu"]

output_dict = {"title":[],
               "location":[],
               "desc":[],
               "price":[],
               "bath":[],
               "bed":[],
               "toilet":[],
               "area":[]}

for location in locations:
    r=requests.get(f"https://nigeriapropertycentre.com/for-rent?keywords={location}&page=1")
    c=r.content

    soup=BeautifulSoup(c,"html.parser")

    card_n = soup.find_all("div", {"class":"col-sm-8 col-xs-12"})[0].text.strip().split(" ")[3]
    card_t = soup.find_all("div", {"class":"col-sm-8 col-xs-12"})[0].text.strip().split(" ")[5]
    try:
        card_n = int(card_n.replace(",",""))
        card_t = int(card_t.replace(",",""))
    except:
        pass
    
    num_pages = math.ceil(int(card_t)/int(card_n))
    print("\n")
    print(f"{location.upper()} has {num_pages} pages")
    
    for page_n in range(1, num_pages+1):
        url = f"www.nigeriapropertycentre.com/for-rent?keywords={location}&page={page_n}"
        r = requests.get("http://"+url)
        c=r.content
        
        soup=BeautifulSoup(c,"html.parser")
        
        #get data for title
        title_list = soup.find_all("h4", {"class":"content-title"})
        for i in range(len(title_list)):
            try:
                output_dict["title"].append(title_list[i].text.strip())
            except:
                output_dict["title"].append("")
        #get data for location
        location_list = soup.find_all("address", {"class":"voffset-bottom-10"})
        for i in range(len(location_list)):
            try:
                output_dict["location"].append(location_list[i].text.strip())
            except:
                output_dict["location"].append("")
        #get data for description
        description_list = soup.find_all("div", {"class":"description hidden-xs"})
        for i in range(len(description_list)):
            try:
                output_dict["desc"].append(description_list[i].find("p").text.strip().replace("\n",""))
            except:
                output_dict["desc"].append("")
        #get data for price
        price_list = soup.find_all("span", {"class":"pull-sm-left"})
        for i in range(len(price_list)):
            try:
                output_dict["price"].append(price_list[i].text.strip().split(" ")[0].replace("₦","").replace(",",""))
            except:
                output_dict["price"].append("")
        #get bath for bedroom
        bed_list = soup.find_all("ul", {"class":"aux-info"})
        for i in range(len(bed_list)):
            try:
                output_dict["bed"].append(re.findall("..Bedrooms", bed_list[i].text)[0])
            except:
                output_dict["bed"].append("")
        #get bath for bath
        bath_list = soup.find_all("ul", {"class":"aux-info"})
        for i in range(len(bath_list)):
            try:
                output_dict["bath"].append(re.findall("..Bathrooms", bath_list[i].text)[0])
            except:
                output_dict["bath"].append("")
        #get bath for toilet
        toilet_list = soup.find_all("ul", {"class":"aux-info"})
        for i in range(len(toilet_list)):
            try:
                output_dict["toilet"].append(re.findall("..Toilets", toilet_list[i].text)[0])
            except:
                output_dict["toilet"].append("")
        for i in range(len(location_list)):
            output_dict["area"].append(location)
        
        #Giving update about scraping
        print(f"{location.upper()} page {page_n} done")
        
        
#converting data to a pandas dataframe
output_df = pd.DataFrame(output_dict)

print(output_df.head())

#save dataframe as csv
output_df.to_csv("Lagos_Real_Estate.csv",index=False)