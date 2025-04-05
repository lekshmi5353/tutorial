import pandas as pd
data = {
    'date': ['2023-04-01', '2023-04-02', '2023-04-03', '2023-04-04', '2023-04-05',
             '2023-04-06', '2023-04-07', '2023-04-08', '2023-04-09', '2023-04-10'],
    'temperature': [30, 25, 28, 22, 27, 31, 29, 24, 26, 23],
    'humidity': [60, 65, 70, 55, 80, 75, 68, 72, 64, 66],
    'windSpeed': [15, 10, 12, 20, 18, 14, 11, 13, 16, 19],
    'precipitationType': ['None', 'Rain', 'None', 'Rain', 'None', 'None', 'Rain', 'None', 'Rain', 'None'],
    'place': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 
              'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin'],
    'weather': ['Sunny', 'Cloudy', 'Sunny', 'Rainy', 'Sunny', 
                'Cloudy', 'Rainy', 'Sunny', 'Rainy', 'Cloudy']
}
df = pd.DataFrame(data)
df.to_csv('weather.csv', index=False)
print("weather.csv file created successfully!")

df = pd.read_csv('weather.csv')

print("First 10 Rows of Weather Data:")
print(df.head(10))


max_temp = df['temperature'].max()
min_temp = df['temperature'].min()
print(f"\nMaximum Temperature: {max_temp}°C")
print(f"Minimum Temperature: {min_temp}°C")


cool_places = df[df['temperature'] < 28]['place']
print("\nPlaces with Temperature < 28°C:")
print(cool_places.tolist())


cloudy_places = df[df['weather'] == 'Cloudy']['place']
print("\nPlaces with Cloudy Weather:")
print(cloudy_places.tolist())


weather_frequency = df['weather'].value_counts().sort_index()
print("\nFrequency of Each Weather Type:")
print(weather_frequency)


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.bar(df['date'], df['temperature'], color='skyblue')
plt.title('Temperature of Each Day')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

