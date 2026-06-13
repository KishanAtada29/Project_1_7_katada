def prefix():
    subnetmasks = {
    'class_A': '255.0.0.0',
    'class_B': '255.255.0.0',
    'class_C': '255.255.255.0'
    }

    for subnetmask in subnetmasks:
        print(f'{subnetmask} : {subnetmasks[subnetmask]}') 

def manual():
    pass

user_choice = input('Please Enter One of the Choice below\nPrefix\tManual\n')
user_choice = user_choice.casefold()
while user_choice != 'prefix' and user_choice != 'manual':
    print('Invalid..')
    user_choice = input('Please Enter One of the Choice below\nPrefix\tManual\n')
    user_choice = user_choice.casefold()


if user_choice == 'prefix':
    prefix()
elif user_choice == 'manual':
    manual()
      


