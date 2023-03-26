# Prompt the user for input
interfacerange = input("Enter interface range (e.g. GigabitEthernet1/0/1-4): ")
channel_group_num = input("Enter channel group number (e.g. 1): ")
active_or_passive = input("Enter LACP mode (active or passive): ")

# Link Aggregation Protocol (LACP)
# passive is detected
# active is unconditionally

# Enable LACP on the following interface
print(f"""
en
config t
interface range {interfacerange}
shutdown
channel-protocol lacp
channel-group {channel_group_num} mode {active_or_passive}
no shutdown
""")

# Enable trunking on LACP channel group
print(f"""
#[enable trunking on LACP channel Group]
en
config t
interface port-channel {channel_group_num}
switchport mode trunk
switchport trunk encapsulatinon dot1q
""")

# Show interfaces
print("show interfaces")

# Show interfaces trunk
print("show interfaces trunk")

# Show etherchannel summary
print("show etherchannel summary")
