# Prompt the user for input
nexthopipv6_or_interface = input("Please enter the next hop IPv6 address or outgoing interface for the default route: ")
destinationnetwork = input("Please enter the destination IPv6 network: ")
nexthopipv6 = input("Please enter the next hop IPv6 address: ")

# Print the IPv6 route commands
print(f"""
# Add a default route using the next hop IPv6 address or outgoing interface
ipv6 route ::/0 {nexthopipv6_or_interface}

# Add a static route using the destination IPv6 network and next hop IPv6 address
ipv6 route {destinationnetwork} {nexthopipv6}
""")
#command means pretty much ipv6 routes for this network thats not us have to go this way

#(default route)
#Device(config)# ipv6 route ::/0 serial 2/0 (default route)
#static
#R1(config)# ipv6 route 2001:DB8::/32   2001:DB8:1:1::1 