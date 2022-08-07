from pathlib import Path

import pandas as pd

from apis.salary_explorer import SalaryExplorerAPI
from apis.trading_economic import TradingEconomicsAPI
from apis.cost_of_living import CostOfLivingAPI
from utilities import read_json


def main() -> None:
    country_config_path = Path().cwd().parent.joinpath('config', 'countries.json')
    countries = read_json(country_config_path)
    
    salary_explorer_api = SalaryExplorerAPI()
    trading_economics_api = TradingEconomicsAPI()
    cost_of_living_api = CostOfLivingAPI()

    columns = ['country', 'currency', 'lowest_salary', 'average_salary',
             'highest_salary', 'inflation_rate_(%)', 'cost_of_living(%)', 
             'purshasing_power(%)']
    df = pd.DataFrame(columns=columns)

    for country_name, metadata in countries.items():
        country_location_code = metadata['location_code']
        salary = salary_explorer_api.get_salaries(country_location_code)
        inflation_rate = trading_economics_api.get_inflation_rate(country_name)
        cost_of_living_indexes = cost_of_living_api.get_cost_of_living_indexes(country_name)

        df.loc[len(df.index)] = [country_name,
                                salary.currency if salary else None,
                                salary.amounts[0] if salary else None, 
                                salary.amounts[1] if salary else None, 
                                salary.amounts[2] if salary else None,
                                inflation_rate,
                                cost_of_living_indexes.cost_of_living_index,
                                cost_of_living_indexes.purchasing_power_index] 
    
    output_file_name = 'country_analysis.xlsx' 
    df.to_excel(output_file_name, index=False)

if __name__ == "__main__": 
    main()