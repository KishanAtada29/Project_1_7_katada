import functions as f
import cidr_desc as cd

def cidr_calculator():
    print('')
    cidr = int(input('Please enter CIDR (0-32): '))
    while cidr > 32 or cidr < 0:
        print('Error...')
        cidr = int(input('Please enter CIDR (0-32): '))


    print('')
    f.result(cidr, cd.cidr_desc(cidr))
   
   

