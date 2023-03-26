interface_name = input("Enter the physical interface name: ")
vlan_number = input("Enter the VLAN number: ")
vlan_router_ip = input("Enter the IP address for the router on this VLAN: ")
vlan_subnet = input("Enter the subnet mask for this VLAN: ")

#this is used when a switch trunk port is conneected to a router


# Configure the subinterface
print(f"""
interface {interface_name}
no shutdown
exit
interface {interface_name}.{vlan_number}
encapsulation dot1q {vlan_number}
ip address {vlan_router_ip} {vlan_subnet}
exit
""")
# Show the routing table to confirm the configuration
print("do show ip route")