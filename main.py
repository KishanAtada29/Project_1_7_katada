subnetmasks = {
    'class_A': '255.0.0.0',
    'class_B': '255.255.0.0',
    'class_C': '255.255.255.0'
}

for subnetmask in subnetmasks:
    print(f'{subnetmask} : {subnetmasks[subnetmask]}') 
