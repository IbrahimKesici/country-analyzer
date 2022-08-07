import json
from pathlib import Path

from apis.salary_explorer import SalaryExplorerAPI
from apis.trading_economic import TradingEconomicsAPI
from utilities import read_json


def main() -> None:
    #salary_explorer_api = SalaryExplorerAPI()
    #salaries = salary_explorer_api.get_salaries(27)
    #print(salaries)
    country_config_path = Path().cwd().parent.joinpath('config', 'countries.json')
    countries = read_json(country_config_path)

    i = 0
    for country_name in countries:
        #trading_economics_api = TradingEconomicsAPI()
        #inflation_rate = trading_economics_api.get_inflation_rate(country_name)

        #print(f'{country_name}: {inflation_rate}')
         

        if i > 3:
            break
        i +=1
  
if __name__ == "__main__": 
    main()