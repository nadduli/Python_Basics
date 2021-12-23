#!/usr/bin/python3

def even(num):
    for i in range(1, num):
        if (num % i) == 0:
            return True
    return False

def max_evens(max_number):
    list_of_evens = []

    for num1 in range(1, max_number):
        if even(num1):
            list_of_evens.append(num1)
    return list_of_evens
result = int(input("Enter maxmium value: "))
list_of_evens = max_evens(result)

for number in list_of_evens:
    print(number)
