#!/usr/bin/python3
'''Defines class MyList'''



class MyList(list):
    '''class inherits from list'''
    
    def print_sorted(self):
        print(sorted(self))
