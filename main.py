
import functions as f
import classful_subnet_info as csi
import cidr_calculator as calculator


        
        



while True:
    print('')
    print('Subnetmask Planner')
    print('-------------------')
    print('')
    print('1. Claseful Subnet Info')
    print('2. Manual CIDR Calculator')
    print('3. Exit')
    print('')
    user_choice = int(input('Please Enter One of the Choice (1-3): '))
    while user_choice != 1 and user_choice != 2 and user_choice != 3:
        print('Invalid option...')
        print('1. Claseful Subnet Info')
        print('2. Manual CIDR Calculator')
        print('3. Exit')
        print('')
        user_choice = int(input('Please Enter One of the Choice (1-3): '))

    
    


    if user_choice == 1:
        csi.classful_subnet()
    elif user_choice == 2:
        calculator.cidr_calculator()
        
    elif user_choice == 3:
        print('Goodbye !')
        break
    print('')
    input('Press Enter to continue...')


