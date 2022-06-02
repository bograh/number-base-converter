'''
AUTHOR  ->   Bernard Ograh
DATE    ->   22nd May, 2022
ABOUT   ->   Convert a number from one base to another
'''
import sys, os, time


def oct_to_dec(num):
    result = int(str(num), 8)
    print(f"0o{num} = {result}")

def bin_to_dec(num):
    result = int(str(num), 2)
    print(f"0b{num} = {result}")

def hex_to_dec(num):
    result = int(str(num), 16)
    print(f"0x{num} = {result}")

def dec_to_bin(num):
    result = bin(int(num))
    print(f"{num} = {result}")

def dec_to_hex(num):
    result = hex(int(num))
    print(f"{num} = {result}")

def dec_to_oct(num):
    result = oct(int(num))
    print(f"{num} = {result}")

def oct_to_bin(num):
    result = int(str(num), 8)
    print(f"0o{num} = {bin(result)}")

def bin_to_oct(num):
    result = int(str(num), 2)
    print(f"0b{num} = {oct(result)}")

def oct_to_hex(num):
    result = int(str(num), 8)
    print(f"0o{num} = {hex(result)}")

def hex_to_bin(num):
    result = int(str(num), 16)
    print(f"0x{num} = {bin(result)}")

def bin_to_hex(num):
    result = int(str(num), 2)
    print(f"0b{num} = {hex(result)}")

def hex_to_oct(num):
    result = int(str(num), 16)
    print(f"0x{num} = {oct(result)}")

def oct_to_hex(num):
    result = int(str(num), 8)
    print(f"0o{num} = {hex(result)}")

def showMenu():
    print("Welcome to Number conversion")
    print(
        '''
    1) Hex to Dec        7) Hex to Oct    
    2) Oct to Dec        8) Hex to Bin    
    3) Bin to Dec        9) Oct to Hex    
    4) Dec to Hex       10) Oct to Bin    
    5) Dec to Oct       11) Bin to Hex    
    6) Dec to Bin       12) Bin to Oct    
        '''
    )

showMenu()

# Validate User Selection of menu choice
try:
    option = int(input("Select and Option: "))

    while option > 12 or option <  1:
        for i in range(1,3):
            print("Invalid choice!")
            option = int(input("Try Again: "))
            if option <= 12 and option >= 1:
                break
        if option <= 12 and option >= 1:
            continue
        print("\nSorry, too many incorrect entries!")
        time.sleep(1.25)
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
        sys.exit()
except ValueError:
    print('You have to enter a number!')
    sys.exit()


def main():
        
    num_to_convert = input("Enter the number you want to convert: ")

    if option == 1:
        hex_to_dec(num_to_convert)
    elif option == 2:
        oct_to_dec(num_to_convert)
    elif option == 3:
        bin_to_dec(num_to_convert)
    elif option == 4:
        dec_to_hex(num_to_convert)
    elif option == 5:
        dec_to_oct(num_to_convert)
    elif option == 6:
        dec_to_bin(num_to_convert)
    elif option == 7:
        hex_to_oct(num_to_convert)
    elif option == 8:
        hex_to_bin(num_to_convert)
    elif option == 9:
        oct_to_hex(num_to_convert)
    elif option == 10:
        oct_to_bin(num_to_convert)
    elif option == 11:
        bin_to_hex(num_to_convert)
    elif option == 12:
        bin_to_oct(num_to_convert)

    hex_arr = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    oct_arr = [str(x) for x in range(0,8)]
    bin_arr = ['0', '1']

    # Check if the number entered is the right format of the number base form chosen

    for i in str(num_to_convert):
        if (option == 1 or option == 7 or option == 8) and i not in hex_arr:
            print('Input not valid for option selected!')
            sys.exit()
        elif (option == 2 or option == 9 or option == 10) and i not in oct_arr:
            print('Input not valid for option selected!')
            sys.exit()
        elif (option == 3 or option == 11 or option == 12) and i not in bin_arr:
            print('Input not valid for option selected!')
            sys.exit()
        elif (option == 4 or option == 5 or option == 6) and i.isdigit() == False:
            print('Input not valid for option selected!')
            sys.exit()


main()