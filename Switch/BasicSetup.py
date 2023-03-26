# Prompt the user for input and store it in variables
hostname = input("Please enter the device hostname: ")
clock_time = input("Please enter the clock time (e.g. 10:10:10 15 september 2016): ")
banner_message = input("Please enter the MOTD banner: ")
enable_password = input("Please enter the enable password: ")
secret_password = input("Please enter the secret password: ")
console_password = input("Please enter the console password: ")
vty_password = input("Please enter the VTY password: ")
password_encryption = input("Do you want to enable password encryption? (y/n): ")
if password_encryption == 'y':
    password_encryption = 'service password-encryption'
else:
    password_encryption = ''
ip_address = input("Please enter the management IP address: ")
subnet = input("Please enter the management subnet: ")
default_gateway = input("Please enter the default gateway: ")
interface = input("Please enter the interface you want to configure: ")
description = input("Please enter a description for the interface: ")
speed = input("Please enter the speed of the interface in KB: ")
mac_statics = input("Do you want to configure a static MAC address? (y/n): ")
if mac_statics == 'y':
    mac_statics = f"mac-address-table static {input('Please enter the MAC address: ')} {input('enter interface that you want to apply static mac address: ')} {input('enter vlan on that interface that will have that staci map address:')}"
else:
    mac_statics = ''

# Basic setup
print(f"""
en
conf t
hostname {hostname}
clock set {clock_time}
banner motd #
{banner_message}#

enable password {enable_password}
enable secret {secret_password}

line console 0
password {console_password}
login
exit

line vty 0 4
password {vty_password}
login
exit

{password_encryption}
""")

# Management interface setup
print(f"""
interface vlan 1
ip address {ip_address} {subnet}
exit
ip default-gateway {default_gateway}
""")

# Interface setup
print(f"""
interface {interface}
description {description}
switchport mode access
speed {speed}
no shutdown
exit
""")

# Web server setup
print(f"""
ip http server
ip http port 80
""")

# Static MAC address setup
print(f"""
{mac_statics}
exit
copy run start
""")

