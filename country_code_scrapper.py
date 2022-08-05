from urllib import response
import requests
import pprint
import json
import re

from bs4 import BeautifulSoup

response = requests.get("http://www.salaryexplorer.com/salary-survey.php")
soup = BeautifulSoup(response.text, "html.parser")


# print(soup.prettify)

countries_to_check = ["Afghanistan","Algeria"]
code_list = {}

# for country in countries_to_check:
#     table = soup.select(f'div.countryselection > b > a')
#     for row in table:
#         if row.get_text() == country.capitalize():
#             location_code = row.get('href').split("?loc=",2)[1].split("&")[0]
#             code_list[country] = {"location_code":location_code}
       

# print(code_list)

# with open('data.json', 'w') as fp:
#     json.dump(code_list, fp)
            
country_div = soup.find("div", {"class": "countryselection"})
for b_tag in country_div.find_all('b'):
    country_name = b_tag.get_text()
    country_href = b_tag.select('a')[0]["href"]
    location_code = re.findall("(?<=loc=)(.*)(?=&)", country_href)
    code_list[country_name] = {"location_code":location_code[0]}
   
with open('data.json', 'w') as fp:
    json.dump(code_list, fp)