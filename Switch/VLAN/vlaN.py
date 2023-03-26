# Prompt the user for input and store it in variables
vlannumber = input("Please enter the VLAN number: ")
vlanname = input("Please enter the VLAN name: ")
vlaninterface = input("Please enter the interface for the VLAN: ")
trunkinterface = input("Please enter the interface for the trunk: ")
desirableorauto = input("Please enter the trunk mode (desirable or auto): ")
allowedVlans = input("Please enter the allowed VLANs (e.g. all, none, except, or a list separated by commas. Default is all): ")

# Creating VLAN
print(f"""
vlan {vlannumber}
name {vlanname}
exit

show vlan

""")

# Assign VLAN to interface
print(f"""

interface {vlaninterface}
switchport mode access
switchport access vlan {vlannumber}
""")

# VLAN Trunking
print(f"""
interface {trunkinterface}
switchport mode trunk
switchport trunk encapsulation dot1q
switchport trunk allowed vlan {allowedVlans}
""")

# Dynamic Trunking
print(f"""
interface {trunkinterface}
switchport mode dynamic {desirableorauto}
""")