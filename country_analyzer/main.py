from apis.salary_explorer import SalaryExplorerAPI

def main() -> None:
    salary_explorer_api = SalaryExplorerAPI(url='http://www.salaryexplorer.com/salary-survey.php')
    salaries = salary_explorer_api.get(27)
    print(salaries)

  
if __name__ == "__main__": 
    main()