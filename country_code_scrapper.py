from urllib import response
import requests
import json
import re

from bs4 import BeautifulSoup

response = requests.get("http://www.salaryexplorer.com/salary-survey.php")
soup = BeautifulSoup(response.text, "html.parser")




countries_to_check = ["Afghanistan","Algeria"]
code_list = {}


            
country_div = soup.find("div", {"class": "countryselection"})
for b_tag in country_div.find_all('b'):
    country_name = b_tag.get_text()
    country_href = b_tag.select('a')[0]["href"]
    location_code = re.findall("(?<=loc=)(.*)(?=&)", country_href)
    code_list[country_name] = {"location_code":location_code[0]}
   
with open('./config/countries.json', 'w') as fp:
    json.dump(code_list, fp)