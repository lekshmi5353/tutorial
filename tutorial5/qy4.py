import pandas as pd
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male'],
    'start_date': ['2020-01-15', '2019-03-22', '2018-07-10', '2021-05-30', '2020-11-12',
                   '2017-09-18', '2019-12-01', '2021-01-25', '2018-04-09', '2022-03-14'],
    'salary': [50000, 60000, 55000, 70000, 62000, 58000, 61000, 64000, 57000, 72000],
    'team': ['Alpha', 'Beta', 'Alpha', 'Gamma', 'Beta', 'Delta', 'Gamma', 'Alpha', 'Delta', 'Beta']
}
df = pd.DataFrame(data)
df.to_csv('employee.csv', index=False)
print("employee.csv file created successfully!")

df = pd.read_csv('employee.csv')


print("First 7 Employee Records:")
print(df.head(7))


sorted_names = df['name'].sort_values()
print("\nEmployee Names in Alphabetical Order:")
print(sorted_names.tolist())


highest_salary_employee = df.loc[df['salary'].idxmax()]['name']
print(f"\nEmployee with the Highest Salary: {highest_salary_employee}")


male_employees = df[df['gender'].str.lower() == 'male']['name']
print("\nNames of Male Employees:")
print(male_employees.tolist())


teams = df['team'].unique()
print("\nTeams Employees Belong To:")
print(teams)
