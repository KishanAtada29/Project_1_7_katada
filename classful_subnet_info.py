import functions as f
import subnetmask_calculator as sc


def class_A():
    network_portion = f.single_octet_bits() * 1
    host_portion = f.single_octet_bits() * 3
    return host_portion, network_portion
def class_B():
    network_portion = f.single_octet_bits() * 2
    host_portion = f.single_octet_bits() * 2
    return host_portion, network_portion
def class_C():
    network_portion = f.single_octet_bits() * 3
    host_portion = f.single_octet_bits() * 1
    return host_portion, network_portion

# In IPv4, 1 represensts network and host represents 0
# class_x [0] = host side
# class_x [1] = network side  

def classful_subnet():
    a = class_A()
    b = class_B()
    c = class_C()
    classful_subnet = {
       'class A':{
           'CIDR': f'/{a[1]}',
           'Number of usable IPs': (2**a[0]) - f.unusable_IPs(),
           'Subnet Mask': f'{".".join(map(str,(sc.subnetmask_calculator(a[1]))))}'
       },
       'class B':{
           'CIDR': f'/{b[1]}',
           'Number of usable IPs': (2**b[0]) - f.unusable_IPs(),
           'Subnet Mask': f'{".".join(map(str,(sc.subnetmask_calculator(b[1]))))}'
        },
        'class C':{
           'CIDR': f'/{c[1]}',
           'Number of usable IPs': (2**c[0]) - f.unusable_IPs(),
           'Subnet Mask': f'{".".join(map(str,(sc.subnetmask_calculator(c[1]))))}'
        }

    }

    for subnetmask, value in classful_subnet.items():
        print('')
        print(subnetmask)
        for label, information in value.items():
            print(f'{label} : {information}')

        print('------------------------') 
