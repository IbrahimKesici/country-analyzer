from locale import currency
import re
from typing import List
from dataclasses import dataclass, field

import requests
from bs4 import BeautifulSoup


@dataclass(repr=True)
class Salary:
    amounts: List[str] = field(default_factory=list)
    currency:str = None
    
class SalaryExplorerAPI:
    
    def __init__(self, url:str="http://www.salaryexplorer.com/salary-survey.php") -> None:
        self._url = url
        self._salary_ranges = ['lowest', 'average', 'highest']

    def get_salaries(self, country_code:int, loc_type:int = 1) -> None:
        url_with_query_params = f'{self._url}?loc={country_code}&loctype={loc_type}'        
        response = requests.get(url_with_query_params)
        response.raise_for_status()

    
        content = self._get_response_content(response.text)
        salaries = self._get_salaries(content)
        return salaries

    def _get_response_content(self, text:str, target_id_tag:str="contentDiv") -> object:
        soup = BeautifulSoup(text, "html.parser")
        content = soup.find(id=target_id_tag)
        return content

    def _get_salaries(self, content:object) -> Salary:
        salary = Salary()
        amounts = []
        for salary_range in self._salary_ranges:
            span = content.find("span", {"class": salary_range})            
            amount, currency = self._exract_salary_info(salary_range, span.text)
            salary.currency = currency
            amounts.append(amount)

        salary.amounts = amounts
            
        return salary

    def _exract_salary_info(self, range:str, text:str) -> Salary:
        content = re.findall('(\d+|[A-Za-z]+)', text)
        amount = "".join([char for char in content if char.isnumeric()])
        currency = content[-1]
        
        return amount, currency