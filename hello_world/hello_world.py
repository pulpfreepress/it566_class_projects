"""Implements the hello_world module.
"""

if __debug__:
    print(f'Debug enabled...')

def say_hi():
    print('Hi!')
    print(f'Module Name: {__name__}')

def print_message(message: str = "Hello, World!")->None:
    print(f'Raw message: {message}')
    print(f'ALL UPPER CASE: {message.upper()}')
    print(f'all lower case: {message.lower()}')
    print(f'Message Length: {len(message)} Characters')
    print(f'Raw message: {message}')

def get_sequence_length(arg:list)->None:
    print(f'List Length: {len(arg)}')

def get_message_from_user()->str:
    user_input = input('Enter a message: ')
    return user_input

def get_number_from_user()->float:
    user_input = input("Enter a number: ")
    result = 0
    try:
         result = float(user_input)
    except Exception as e:
        print(f'Invalid number. Setting result to zero.')

    return result
