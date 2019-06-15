def create_fibinacci(limit):
    fibonacci_array = [0,1]

    fib = 0
    while (fib < limit):
        fib = fibonacci_array[-1] + fibonacci_array[-2]
        fibonacci_array.append(fib)

    print("Fibonacci array till limit is \n",fibonacci_array)

if '__name__' == '__main__':
    fibonacci_limit = input("Enter a number till which you need a fibonacci")
    create_fibinacci(100)

