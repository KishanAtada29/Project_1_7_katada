"""
    Program Name: Subnet Planner
    Author: Kishan Atada
    Purpose: Collect and validate CIDR input, then display subnet information.
    Starter Code Information: No starter code was used.
    Date: June 23, 2026
"""

import functions as f
import cidr_desc as cd

def cidr_calculator():
    """
    Ask the user for a CIDR prefix and display the subnet information.

    The function validates that the CIDR value is between 0 and 32.
    """
    print('')
    cidr = int(input('Please enter CIDR (0-32): '))
    while cidr > 32 or cidr < 0:
        print('Error...')
        cidr = int(input('Please enter CIDR (0-32): '))


    print('')
    f.get_result(cidr, cd.cidr_desc(cidr))
   
   

