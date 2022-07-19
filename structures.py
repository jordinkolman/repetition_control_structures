'''
Created on Tuesday Jul 19 15:01 2022

@author: Jordin Kolman
'''

def even_numbers():
    test_number = 0
    while (0 <= test_number <= 100):
        if (test_number % 2 == 0):
            print(test_number)
            test_number = test_number + 1
        else:
            test_number = test_number + 1

even_numbers()