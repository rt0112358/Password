from termcolor import colored
import random
#################################################
# Random password generator
#
# @author rt0112358
#################################################

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

print()
print(colored(output, 'cyan', attrs=['bold']))
print()
