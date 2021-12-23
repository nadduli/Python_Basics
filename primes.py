#!/usr/bin/python3
# print a list of prime numbers

def prime(num):
    for i in range(2, num):
        if(num % i) == 0:
            return False
    return True

def get_prime(max_num):
    list_of_primes = []

    for num1 in range(2, max_num):
        if prime(num1):
            list_of_primes.append(num1)
    return list_of_primes

max_value = int(input("Search for max value: "))

list_of_primes = get_prime(max_value)
for primez in list_of_primes:
    print(primez)
