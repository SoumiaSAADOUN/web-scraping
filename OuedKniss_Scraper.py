import requests
import json
import csv
from bs4 import BeautifulSoup as bs

# create the files where to put the extracted data
csvFile = open("ouedknissData.csv", "w", encoding="utf8")
jsonFile = open ("ouedknissData.json", "w", encoding="utf8")
# set the url of the web site we want to webscrap
url= "https://www.ouedkniss.com/telephones/"
# open a json object
jsonFile.write("[/n")
data={}
csv_cols = {"name", "price", "details"}
for page in range (1):
 	read = requests.get(url + str(page+1))
 	soup = bs(read.content, "html.parser")  # to read the html in read, to access the html of the page 
 	ancher = soup.find_all("ul", {"class": "annonce_left"})  #the div that contains all the infrmations I need, returns an array
 	writer = csv.DictWriter(csvFile, fieldnames = csv_cols)
 	i=0
 	writer.writeheader()
 	for point in ancher:
 		name= point.find("h2", {"itemprop": "name"})
 		price= point.find("span", {"itemprop":"price"})
 		details = point.find("a", {"class":"annonce_image_img"}).attrs["href"]
 		if price:
 			writer.writerow({"name": name.text.replace("     ", "").strip("\r\n"), "price": price.text, "details": details})
 			data["name"]= name.text.replace("     ", "").strip("\r\n")
 			data["price"]= price.text
 			data["details"]= details
 			jsonData= json.dumps(data, ensure_ascii=False)
 			jsonFile.write(jsonData)
 			jsonFile.write(",/n")
jsonFile.write(" /n]")
csvFile.close()
jsonFile.close() 		



