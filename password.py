from termcolor import colored
import random
#########################################
# Random password generator
#########################################

# Generate random password with
# uppercase letters, lowercase letters,
# and numbers.
def get_password():
    characters = 'abcdefghijklmnopqrstuvwxyz'
    capitals = characters.upper()
    numbers = '0123456789'
    output = ''

    for i in range(14):
        choice = random.randint(0,2)
        if(choice == 0):
            output += characters[random.randint(0,25)]
        elif(choice == 1):
            output += capitals[random.randint(0,25)]
        elif(choice == 2):
            output += numbers[random.randint(0,9)]
        else:
            print("Something blew up")
    return output

def print_password():
    psswrd = get_password()
    # print()
    print(colored(psswrd, 'cyan', attrs=['bold']))
    # print()
    # return psswrd

#TODO: add special characters to password generator