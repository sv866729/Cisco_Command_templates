#protect documetns and counts port violations doesnt display on cosole
#resrict document and conutns port violations does display violations
#shutdown shuts down interface if a violation occurs
#vilations are incorrect mac addresses plugged into port



interface = input("Please enter the name of the interface: ")
staticmac = input("Please enter the static MAC address: ")
protect_restrict_shutdown = input("Please choose one of the following options for port security: protect, restrict, or shutdown: ")

# Configure interface with static MAC address
print(f"""
[static]
en 
configuration
interface {interface}
switchport mode access
switchport port-security
switchport port-security mac-address {staticmac}
switchport port-security {protect_restrict_shutdown}
""")

# Configure interface with sticky MAC address

print(f"""
[Dynamic]
en 
configuration
interface {interface}
switchport mode access
switchport port-security
switchport port-security mac-address sticky
switchport port-security {protect_restrict_shutdown}
""")

# Show port-security configuration
print(f"""
[configuration]
show port-security
# or 
show port-security interface {interface}
""")
