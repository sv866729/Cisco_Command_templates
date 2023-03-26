#VTP auto updates vlans on connceted devices

# Prompt the user for input and store it in variables
domainname = input("Please enter the VTP domain name: ")
vtp_pass = input("Please enter the VTP password: ")
interface_connectingtoserver = input("Please enter the interface connecting to the VTP server: ")
nativevlan = input("Please enter the native VLAN for the trunk port: ")

# VTP Server Setup
print(f"""
vtp mode server
vtp domain {domainname}
vtp password {vtp_pass}


""")

# VTP Client Setup
print(f"""
vtp mode client
vtp domain {domainname}
vtp password {vtp_pass}
interface {interface_connectingtoserver}
switchport mode trunk
switchport trunk native vlan {nativevlan}
""")
