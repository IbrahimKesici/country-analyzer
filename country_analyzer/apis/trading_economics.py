import requests
from bs4 import BeautifulSoup

class TradingEconomics:

    def __init__(self, country_name):
        self.country_name = country_name
        self.url = "https://tradingeconomics.com/country-list/inflation-rate?continent=world"

    def get_html_of_page(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")