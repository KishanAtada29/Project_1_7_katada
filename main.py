def class_A():
    return 24
def class_B():
    return 16
def class_C():
    return 8
def prefix_bits():
    numbers = [128, 64, 32, 16, 8, 4, 2, 1]
    return numbers
def single_octet_bits():
    return 8
def number_of_octets():
    return 4
def total_bits():
    return (single_octet_bits() * number_of_octets())
def remaing_bits(n):
    return total_bits() - n   
def unusable_IPs():
    return 2
def octect_value():
    return sum(prefix_bits())
def usable_ip(num):
    num = total_bits() - num
    num = (unusable_IPs() ** num) - unusable_IPs()
    return num
def classful_subnet():
    classful_subnet = {
       'class A':{
           'CIDR': '/8',
           'Number of usable IPs': (2**class_A()) - unusable_IPs(),
           'Subnetmask': '255.0.0.0'
       },
       'class B':{
           'CIDR': '/16',
           'Number of usable IPs': (2**class_B()) - unusable_IPs(),
           'Subnetmask': '255.255.0.0'
        },
        'class C':{
           'CIDR': '/24',
           'Number of usable IPs': (2**class_C()) - unusable_IPs(),
           'Subnetmask': '255.255.255.0'
        }

    }

    for subnetmask, value in classful_subnet.items():
        print('')
        print(subnetmask)
        for label, information in value.items():
            print(f'{label} : {information}')

        print('------------------------') 

def manual():
    print('')
    cidr = int(input('Please enter CIDR (0-32): '))
    while cidr > 32 or cidr < 0:
        print('Error...')
        cidr = int(input('Please enter CIDR (0-32): '))
    octect = 0
    subnetmask = []
    if cidr == 0:
        subnetmask = [0,0,0,0]
        print('')
        print(f'Address: {".".join(map(str,(subnetmask)))} /{cidr}')
        print(f'Total IPv4 Address: {usable_ip(cidr) + unusable_IPs()} ')
        print('Description: /0 represents all IPv4 address and is commonly used as a default route')
    else:
        octet_side = cidr % single_octet_bits()
        each_octet = int(cidr / 8)
        for bit in range(each_octet):
            subnetmask.append(sum(prefix_bits()))
        for bit in range(octet_side):
            octect = prefix_bits()[bit] + octect
        subnetmask.append(octect)
        if len(subnetmask) == 3:
            subnetmask.append(0)
        elif len(subnetmask) == 2:
            subnetmask.append(0)
            subnetmask.append(0)
        elif len(subnetmask) == 1:
            subnetmask.append(0)
            subnetmask.append(0)
            subnetmask.append(0)
        elif len(subnetmask) == 5:
            subnetmask.pop()


        print(f'CIDR: /{cidr}')
        print(f'Nuber of useable host: {usable_ip(cidr)}')
        print(f'Subnetmask: {".".join(map(str,(subnetmask)))}')

        

        
        



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
        classful_subnet()
    elif user_choice == 2:
        manual()
        
    elif user_choice == 3:
        print('Goodbye !')
        break
    print('')
    input('Press Enter to continue...')


