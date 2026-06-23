"""
    Program Name: Subnet Planner
    Author: Kishan Atada
    Purpose: Provide classful subnet information and calculate subnet masks
    from CIDR prefixes.
    Starter Code Information: No starter code was used.
    Date: June 23, 2026
"""

import classful_subnet_info as csi
import cidr_input as ci
import functions as f        


while True:
    print('')
    print('Subnetmask Planner')
    print('-------------------')
    print('')
    f.display_menu()
    print('')
    user_choice = int(input('Please Enter One of the Choice (1-3): '))
    print('')
    while user_choice not in [1,2,3]:
        print('')
        print('Invalid option...')
        print('')
        f.display_menu()
        print('')
        user_choice = int(input('Please Enter One of the Choice (1-3): '))

    
    


    if user_choice == 1:
        csi.classful_subnet()
    elif user_choice == 2:
        ci.cidr_calculator()
        
    elif user_choice == 3:
        print('')
        print('Goodbye !')
        print('')
        break
    print('')
    input('Press Enter to continue...')


