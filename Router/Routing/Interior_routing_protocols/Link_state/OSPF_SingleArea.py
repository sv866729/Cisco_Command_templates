# Prompt user for input and store in variables
networkID = input("Enter the network ID to be broadcasted (e.g. 192.168.1.0): ")
wildcardsubnetmask = input("Enter the wildcard subnet mask (e.g. 0.0.0.255): ")
areaID = input("Enter the area ID for the network (e.g. 0): ")
netowwordID_2 = input("Enter the second network ID to be broadcasted (e.g. 10.0.0.0): ")
wildcarsubnetmask2 = input("Enter the second wildcard subnet mask (e.g. 255.255.255.0): ")
passinterface = input("Enter the interface to set as passive (e.g. GigabitEthernet0/0): ")

# Thenetworks are the networks that the router needs to broadcast
print(f"""
en
config t
router ospf
network {networkID} {wildcardsubnetmask} area {areaID}
network {netowwordID_2} {wildcarsubnetmask2} area {areaID}""")

# Setting passive interface on an interface not connected to a router, such as a switch
# This allows updates but won't send updates via that interface
print(f"router ospf \n passive-interface {passinterface}")

# Routers are only aware of directly connected routers
# Area 0 is the backbone area
# Each interface is assigned an area
