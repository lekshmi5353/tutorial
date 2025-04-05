import pandas as pd
data = {
    'rollno': [101, 102, 103, 104, 105],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'place': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
    'mark': [85, 90, 78, 88, 92]
}
df = pd.DataFrame(data)
df.to_csv('stud.csv', index=False)
print("stud.csv file created successfully!")

df = pd.read_csv('stud.csv')

print("File Contents:")
print(df)

df.set_index('rollno', inplace=True)
print("\nData with rollno as Index:")
print(df)

print("\nName and Mark:")
print(df[['name', 'mark']])

sorted_by_name = df.sort_values(by='name')
print("\nSorted by Name:")
print(sorted_by_name[['name', 'mark']])

sorted_by_mark_desc = df.sort_values(by='mark', ascending=False)
print("\nSorted by Mark (Descending):")
print(sorted_by_mark_desc[['name', 'mark']])

average_mark = df['mark'].mean()
median_mark = df['mark'].median()
mode_mark = df['mark'].mode().values[0]
print(f"\nAverage Mark: {average_mark}")
print(f"Median Mark: {median_mark}")
print(f"Mode Mark: {mode_mark}")

min_mark = df['mark'].min()
max_mark = df['mark'].max()
print(f"\nMinimum Mark: {min_mark}")
print(f"Maximum Mark: {max_mark}")


variance_mark = df['mark'].var()
std_deviation_mark = df['mark'].std()
print(f"\nVariance of Marks: {variance_mark}")
print(f"Standard Deviation of Marks: {std_deviation_mark}")


import matplotlib.pyplot as plt
plt.hist(df['mark'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()


df = df.drop(columns=['place'])
print("\nData after Removing 'place' Column:")
print(df)
