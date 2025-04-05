import pandas as pd
data = {
    'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'facecream': [150, 180, 200, 170, 190, 220, 250, 230, 210, 200, 190, 180],
    'facewash': [120, 130, 140, 110, 150, 160, 180, 170, 160, 140, 130, 125],
    'toothpaste': [300, 320, 310, 330, 350, 360, 340, 330, 310, 300, 290, 280],
    'bathingsoap': [200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310],
    'shampoo': [180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290],
    'moisturizer': [90, 95, 100, 85, 110, 115, 120, 125, 130, 135, 140, 145],
    'total_units': [1040, 1110, 1170, 1160, 1260, 1375, 1410, 1415, 1360, 1265, 1280, 1310],
    'total_profit': [5000, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200]
}
df = pd.DataFrame(data)
df.to_csv('sales.csv', index=False)
print("sales.csv file created successfully!")


df = pd.read_csv('sales.csv')


import matplotlib.pyplot as plt
plt.figure(figsize=(10, 5))
plt.scatter(df['month_number'], df['toothpaste'], color='blue')
plt.title('Toothpaste Sales Data (Monthly)')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 5))
width = 0.35  
x = df['month_number']
plt.bar(x - width/2, df['facecream'], width, label='Face Cream', color='orange')
plt.bar(x + width/2, df['facewash'], width, label='Face Wash', color='cyan')
plt.title('Face Cream & Face Wash Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Units Sold')
plt.xticks(x)
plt.legend()
plt.show()


total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()
plt.figure(figsize=(8, 8))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
plt.title('Total Sales Distribution for Each Product')
plt.show()
