import functions as f
import subnetmask_calculator as sc

def cidr_calculator():
    print('')
    cidr = int(input('Please enter CIDR (0-32): '))
    while cidr > 32 or cidr < 0:
        print('Error...')
        cidr = int(input('Please enter CIDR (0-32): '))
    if cidr == 0:
        print('')
        f.result(cidr)
        print('Description: /0 represents all IPv4 address and is commonly used as a default route')
    #elif cidr == 31
    else:
        print('')
        f.result(cidr)
   

