from __future__ import absolute_import, division, print_function
from getpass import getpass
#This code come from Grelleum //youtube// (network automate - 07 No video)

def get_input(prompt=''):
    try:
        line = input(prompt)
    except NameError:
        line = input(prompt)
    return line   

def get_credential():
    '''Prompts for, and returns, a username and password'''
    username = get_input('Enter Username: ')
    password = None 
    while not password
        password = getpass()
        password_verify = getpass('Retype your password: ')
        if password != password_verify
        print('Password do not match, Try Again.')
        password = None
        return username, password

        