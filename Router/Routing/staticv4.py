#how to set static rout
#Default admin distannce is 1 if u set it higher 1-100 it will be considered a backup route

# Prompt the user for input
destination_network = input("Please enter the destination network: ")
destination_subnet = input("Please enter the destination subnet mask: ")
nexthopip = input("Please enter the next hop IP address: ")
administrative_distance = input("Please enter the administrative distance (default is 1): ")
current_router_exit_interface = input("Please enter the current router exit interface: ")


# Print the static route commands
print(f"""
# Add a static route using the destination network, subnet mask, next hop IP, and administrative distance
ip route {destination_network} {destination_subnet} {nexthopip} {administrative_distance}

# Add a static route using the destination network, subnet mask, current router exit interface, and administrative distance
ip route {destination_network} {destination_subnet} {current_router_exit_interface} {administrative_distance}

# Add a default route or route of last resort using the next hop IP
ip route 0.0.0.0 0.0.0.0 {nexthopip}

# Show the IP routes
show ip route
""")


