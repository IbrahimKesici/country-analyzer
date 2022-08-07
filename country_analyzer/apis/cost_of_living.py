from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup


@dataclass(repr=True)
class CostOfLivingIndex:
    purchasing_power_index: int
    cost_of_living_index: int

class CostOfLivingAPI:

    def __init__(self, url:str='https://www.numbeo.com/cost-of-living/rankings_by_country.jsp') -> None:
        self._url = url
        self._cost_of_living_by_countries = {}

    
    def get_cost_of_living_indexes(self, country_name:str) -> None:
        if not self._cost_of_living_by_countries:
            website_content = self._make_request()
            soup = BeautifulSoup(website_content, "html.parser")
            self._extract_all_cost_of_living_data(soup)

        empty_cost_of_living_index =  CostOfLivingIndex(purchasing_power_index=None, cost_of_living_index=None)
        return self._cost_of_living_by_countries.get(country_name.lower()) or empty_cost_of_living_index

    def _make_request(self) -> str:
        response = requests.get(self._url)
        response.raise_for_status()

        return response.text
    
    def _extract_all_cost_of_living_data(self, content:object) -> None:
        for row in content.find_all('tr', {"style": "width: 100%"}):
            columns = row.find_all('td')
            
            country_name = columns[1].text.lower()
            cost_of_living_index = CostOfLivingIndex(purchasing_power_index=columns[-1].text, 
                                                    cost_of_living_index=columns[4].text)
            
            
            self._cost_of_living_by_countries[country_name] = cost_of_living_index
