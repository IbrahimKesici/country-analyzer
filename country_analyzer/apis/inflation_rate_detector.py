

from ast import Break
from traceback import print_tb
import requests
from bs4 import BeautifulSoup

class InflationRateResearcher:

    def __init__(self, country_name, url="https://tradingeconomics.com/country-list/inflation-rate?continent=world"):
        self.country_name = country_name
        self.url = url

    def inflation_rate(self):
        soup_element = self.html_parser(self.url)
        inflation_rate, country = self.datatable_filter(soup_element, self.country_name)
        print(f"Inflation rate for {country} is {inflation_rate}")
        return inflation_rate

    @staticmethod
    def html_parser(url):
        session = requests.Session()
        response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        return BeautifulSoup(response.text, "html.parser")

    @staticmethod
    def datatable_filter(soup_element, country):

        for tr_tag in soup_element.find_all("tr"):
            a_tag = tr_tag.select("tr > td > a")

            if a_tag:
                rate_tag = tr_tag.select("tr > td > span.te-value-negative")
                if not rate_tag:
                    rate_tag = tr_tag.find_all("td", {"data-heatmap-value" : True})
                if a_tag[0].get_text().strip().lower() == country.lower():
                    found_country_name = a_tag[0].get_text().strip()
                    return rate_tag[0].get_text(), found_country_name
          


inflation = InflationRateResearcher("Benin")
inflation_rate = inflation.inflation_rate()