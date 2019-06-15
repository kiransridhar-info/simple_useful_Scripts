def factorial(number):
    factorialVal = 1
    if number == 0:
        print("Factorial of %s is 1" %number)
    else:
        for n in range(1,number+1):
            factorialVal = factorialVal * n
        print("Factorial of %s is %s" % (number, factorialVal))

if __name__ == '__main__':
     number_to_which_factorial_is_required = int(input("Input the number for which factorial is required"))
     factorial(number_to_which_factorial_is_required)