import requests
from bs4 import BeautifulSoup as bs
import csv
from itertools import zip_longest

# the file that will contain the job offers
jobsFile = open("jobsFile.csv","w",encoding="utf8")
csv_cols = {"title", "company", "location", "skills"}
writer = csv.DictWriter(jobsFile, fieldnames = csv_cols)
writer.writeheader()
# get the url 
result = requests.get('https://wuzzuf.net/search/jobs/?a=hpb%7Cspbg&q=python%20developer')
# get the result's content, markup
content = result.content
# create a soup object to parse content (lxml parser)
soup = bs(content,"lxml")

# find the element we need 
job_details= soup.find_all("div", {"class":"css-9hlx6w"})
for point in job_details:
	skills =[]
	job_title= point.find("h2", {"class": "css-m604qf"})
	job_company_name= point.find("a",{"class":"css-17s97q8"})
	job_location = point.find("span", {"class": "css-5wys0k"})
	job_skills = point.find("div", {"class":"css-y4udm8"})
	job_skills = job_skills.find_all("a", {"class": "css-nn640c"})
	for skill in job_skills:
		skills.append(skill.text)
	writer.writerow({"title": job_title.text, "company": job_company_name.text, "location": job_location.text, "skills": skills})	
jobsFile.close()	



