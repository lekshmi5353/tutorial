import pandas as pd
df = pd.read_csv('auto.csv')
print(df.head())

df.columns = df.columns.str.strip()
df = df.dropna()  
df['company'] = df['company'].replace({'Toyta': 'Toyota'})
df.to_csv('auto_cleaned.csv', index=False)
print("Data cleaned and saved to 'auto_cleaned.csv'")

most_expensive = df[df['price'] == df['price'].max()]['company'].values[0]
print(f"Most Expensive Car Company: {most_expensive}")

toyota_cars = df[df['company'].str.contains('Toyota', case=False, na=False)]
print(toyota_cars)

car_counts = df['company'].value_counts()
print(car_counts)

highest_priced_car = df.loc[df['price'].idxmax()]
print("Highest Priced Car Details:")
print(highest_priced_car)

# Assuming 'average-mileage' is the column name
average_mileage = df.groupby('company')['average-mileage'].mean()
print("Average Mileage by Company:")
print(average_mileage)

sorted_cars = df.sort_values(by='price', ascending=False)
print("Cars sorted by Price:")
print(sorted_cars)
