#!/usr/bin/python3

""" calculate the compound interest after 10 years
"""
principle = input('Enter amount of money to invest: ')
interest_rate = input('Enter the Interest Rate: ')

principle = float(principle)

interest_rate = float(interest_rate) * .01
for i in range (10):
    principle = principle + (principle * interest_rate)
print ("Amount invested after a decade: Shs {:.2f}".format(principle))
