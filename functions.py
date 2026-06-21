import subnetmask_calculator as sc

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


def result(cidr,desc):
    print(f'CIDR: /{cidr}')
    print(f'Nuber of useable host: {usable_ip(cidr)}')
    print(f'Subnetmask: {".".join(map(str,(sc.subnetmask_calculator(cidr))))}')
    print('Description: ' + desc)

