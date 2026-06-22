"""Converts a CIDR prefix into a four-octet subnet mask."""

import functions as f

def subnetmask_calculator(cidr):
    """
    Convert a CIDR prefix into a subnet mask.

    Args:
        cidr: An integer from 0 to 32.

    Returns:
        A list containing four subnet-mask octets.
    """
    subnetmask = [] 
    if cidr == 0:
        subnetmask = [0,0,0,0]
    else:
        octect = 0
        octet_side = cidr % f.single_octet_bits()
        each_octet = int(cidr / f.single_octet_bits())
        for bit in range(each_octet):
            subnetmask.append(sum(f.prefix_bits()))
        for bit in range(octet_side):
            octect = f.prefix_bits()[bit] + octect
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
        
    return subnetmask
