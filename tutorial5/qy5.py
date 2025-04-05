import pandas as pd
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Branch': ['CSE', 'ECE', 'CSE', 'ME', 'CSE', 'EEE', 'ME', 'CSE', 'EEE', 'CSE'],
    'Year': [2, 3, 2, 4, 1, 3, 4, 2, 1, 3],
    'CGPA': [9.1, 8.5, 9.5, 7.8, 9.2, 8.9, 7.5, 9.8, 8.7, 9.3]
}
df = pd.DataFrame(data)
df.to_csv('student.csv', index=False)
print("student.csv file created successfully!")


df = pd.read_csv('student.csv')


average_cgpa = df['CGPA'].mean()
print(f"Average CGPA of Students: {average_cgpa:.2f}")


high_cgpa_students = df[df['CGPA'] > 9]
print("\nStudents with CGPA > 9:")
print(high_cgpa_students)


cse_high_cgpa_students = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print("\nCSE Students with CGPA > 9:")
print(cse_high_cgpa_students)


max_cgpa_student = df.loc[df['CGPA'].idxmax()]
print("\nStudent with Maximum CGPA:")
print(max_cgpa_student)


average_cgpa_by_branch = df.groupby('Branch')['CGPA'].mean()
print("\nAverage CGPA by Branch:")
print(average_cgpa_by_branch)
