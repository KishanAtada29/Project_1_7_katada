
import functions as f

def subnetmask_calculator(cidr):
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
