fibonacci = [0, 1]
for i in range(8):
    fibonacci.append(fibonacci[-1] + fibonacci[-2])
print("First 10 Fibonacci numbers:", fibonacci)
