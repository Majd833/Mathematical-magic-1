def print_factors(number):
    for i in range(1,number+1):
        if number%i==0:
            print(i)
number=int(input("Enter the number that you want to find it's factors:"))
print_factors(number)