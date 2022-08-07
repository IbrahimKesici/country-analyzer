from itertools import count
from pathlib import Path

from apis.salary_explorer import SalaryExplorerAPI
from apis.trading_economic import TradingEconomicsAPI
from apis.cost_of_living import CostOfLivingAPI
from utilities import read_json


def main() -> None:
    #salary_explorer_api = SalaryExplorerAPI()
    #salaries = salary_explorer_api.get_salaries(27)
    #print(salaries)
    country_config_path = Path().cwd().parent.joinpath('config', 'countries.json')
    countries = read_json(country_config_path)
    #trading_economics_api = TradingEconomicsAPI()
    cost_of_living_api = CostOfLivingAPI()

    i = 0
    for country_name in countries:
        #inflation_rate = trading_economics_api.get_inflation_rate(country_name)
        
        #print(f'{country_name}: {inflation_rate}')

        cost_of_living_indexes = cost_of_living_api.get_cost_of_living_indexes(country_name)
        print(cost_of_living_indexes)
       
        if i > 3:
            break
        i +=1
  
if __name__ == "__main__": 
    main()