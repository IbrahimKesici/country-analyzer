import requests
from bs4 import BeautifulSoup


class TradingEconomicsAPI:
    """ Interface to get inflation rate by countries """

    def __init__(self, url:str="https://tradingeconomics.com") -> None:
        self._url = url
        self._headers ={'User-Agent': 'Mozilla/5.0'}

    def get_inflation_rate(self, country_nane:str) -> None:
        try:
            cleaned_country_name = country_nane.lower().replace(' ', '-')
            url_with_query_params = f'{self._url}/{cleaned_country_name}/inflation-cpi'   
            print(url_with_query_params)
            content = self._make_request(url_with_query_params)

            soup = BeautifulSoup(content, "html.parser")
            inflation_rate = self._extract_inflation_rate(soup)
            return inflation_rate
        except Exception as e:
            print(e)
            return None

    def _make_request(self, url:str) -> str:
        session = requests.Session()
        response = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}, verify=False)
        response.raise_for_status()
        
        return response.text

    def _extract_inflation_rate(self, soup:object) -> str:
        for tr in soup.find_all('tr', {'class': 'datatable-row'}):
            if 'inflation rate' in tr.text.lower():
                inflation_rate = tr.find_all('td')[1].text
                return inflation_rate