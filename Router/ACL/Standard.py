#Standard Access List (ACL)
# – permit/deny only traffic “coming from” [source] - a specific
# IP addresses or network 
#Router(config)#access-list {number} {permit / deny} {source address}

number1_99 = input("Enter an ACL number (1-99): ")
permit_deny = input("Enter whether to 'permit' or 'deny' traffic: ")
host_address = input("Enter the host IP address to be filtered (e.g. 192.168.1.1): ")
networkID = input("Enter the network ID to be filtered (e.g. 192.168.1.0): ")
wildcard_subnet = input("Enter the wildcard subnet mask (e.g. 0.0.0.255): ")
inteface = input("Enter the interface name (e.g. GigabitEthernet0/0): ")
in_out = input("Enter whether the ACL should be applied 'in' or 'out' on the interface: ")

#Router(config)#access-list {number} {permit / deny} {source address}
print(f"""en
config t
#host ACL
access-list {number1_99} {permit_deny} host {host_address} """)

#Router(config)#access-list {number} {permit / deny} {source address} [wildcard-mask]
print(f"""en
config t
#network ACL
access-list {number1_99} {permit_deny} {networkID} {wildcard_subnet}""" )

# Apply ACL to interface
print(f"""
[set to interface]
interface {inteface}
ip access-group {number1_99} {in_out}""")

# Implicit deny at the end of ACL
print("""
#implicit Deny
Access-list 1 deny ANY
#allow any traffic that does not match the ACL
access-list 1 permit any""")

# Display the access-list, IP access-list, interface, and running-configuration
print(f"""
Show access-list 

Show ip access-list 

Show ip interface 

Show running-configuration  """)