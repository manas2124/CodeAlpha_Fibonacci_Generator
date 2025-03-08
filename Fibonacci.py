
# Function to generate Fibonacci sequence using recursion
def fibonacci_recursive(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    series = fibonacci_recursive(n - 1)
    series.append(series[-1] + series[-2])
    return series


# Function to generate Fibonacci sequence using iteration
def fibonacci_iterative(n):
    if n <= 0:
        return "Invalid input"
    series = [0, 1]
    for _ in range(2, n):
        series.append(series[-1] + series[-2])
    return series

if __name__ == "__main__":
    n = int(input("Enter the number of terms for Fibonacci series: "))
    print("Recursive Fibonacci:", fibonacci_recursive(n))
    print("Iterative Fibonacci:", fibonacci_iterative(n))
