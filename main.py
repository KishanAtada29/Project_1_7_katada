def class_A():
    return 24
def class_B():
    return 16
def class_C():
    return 8
    
def prefix():
    subnetmasks = {
       'class A':{
           'CIDR': '/8',
           'Number of usable IPs': (2**class_A()) -2,
           'Subnetmask': '255.0.0.0'
       },
       'class B':{
           'CIDR': '/16',
           'Number of usable IPs': (2**class_B()) - 2,
           'Subnetmask': '255.255.0.0'
        },
        'class C':{
           'CIDR': '/24',
           'Number of usable IPs': (2**class_C()) - 2,
           'Subnetmask': '255.255.255.0'
        }

    }

    for subnetmask, value in subnetmasks.items():
        print(subnetmask)
        for label, information in value.items():
            print(f'{label} : {information}')

        print('------------------------') 

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
      


