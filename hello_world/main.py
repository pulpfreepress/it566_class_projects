"""Implements Hello World demo."""

import hello_world

# So does this one, but this is a function definition
def main():
    # message = hello_world.get_message_from_user()
    # hello_world.print_message(message)
    number = hello_world.get_number_from_user()
    print(f'User entered: {number}')
    print('User entered: ' + str(number))
   

if __name__ == "__main__":
    main()