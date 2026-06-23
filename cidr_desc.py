"""
    Program Name: Subnet Planner
    Author: Kishan Atada
    Purpose: Provide classful subnet information and calculate subnet masks
        from CIDR prefixes.
    Starter Code Information: No starter code was used.
    Date: June 23, 2026
"""

def cidr_desc(cidr):
    """
    Return a short description for a CIDR prefix.

    Args:
        cidr: An integer from 0 to 32.

    Returns:
        A string describing the common use of the CIDR range.
    """
    if cidr == 0:
        des = 'Represents all IPv4 addresses; commonly used as a default route.'
    elif 1 <= cidr <= 7:
        des = 'Extremely large address ranges, rarely used as normal LAN subnets.'
    elif 8 <= cidr <= 15:
        des = 'Very large networks.'
    elif 16 <= cidr <= 23:
        des = 'Commonly used for Medium-to-large networks.'
    elif 24 <= cidr <= 29:
        des = 'Commonly used for LANs and smaller subnets.'
    elif cidr == 30:
        des = 'Traditionally used for point-to-point links; provides 2 usable hosts.'
    elif cidr == 31:
        des = 'Used for point-to-point links; both address are useable.'
    elif cidr == 32:
        des = 'Represents one specific IPv4 address, often used as a host route.'
    
    return des