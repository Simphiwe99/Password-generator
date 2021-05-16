import linecache
import random


## def file_reader():
##a_file = open("pass.txts","r")
##list_of_lists = []
##for line in a_file:
##    stripped_line = line.strip()
##    line_list+ stripped_line.split()
##    list_of_lists.append(line_list)

##a_file.close()
##print(list_of_lists)

def file_reader():
    filename = "pass.txt"

    linenumber1 = 1
    linenumber2 = 2
    linenumber3 = 3

    line1 = linecache.getline(filename, linenumber1)
    line2 = linecache.getline(filename, linenumber2)
    line3 = linecache.getline(filename, linenumber3)
    return line1, line2, line3


def input_requirements():
    length = int(input("Please enter the num characters! :"))  # This code is input
    satisfied = input("Are you satisfied with the new password?, please enter yes or no")
    return length, satisfied


def in_array():
    letter, digits, symbols = file_reader()
    lists = []
    lists.append(letter)
    lists.append(digits)
    lists.append(symbols)

    return letter, digits, symbols


def password_generator():
    l, d, s = inArray()
    l, d, s = True, True, True

    letter = l
    digits = d
    symbols = s
    all = ""

    if l:
        all += letter
    if d:
        all += digits
    if s:
        all += symbols

    leng, sat = input_requirements()
    amount = 3
    for x in range(amount):
        password = "".join(random.sample(all, leng))
        print(password)

    count = 0


while True:
    count += 1
    final = password_generator()
    if final != "false":
        print("Your new password is: " + str(final))

        if sat == "yes":
            print("password accepted")
            break
        elif sat == 'no':
            count += 1
            final = password_generator()
            print(final)
            continue
    if count == 3:
        print('Limit has been exceeded')
        break

    file_reader()
    input_requirements()
    inArray()
    password_generator()
