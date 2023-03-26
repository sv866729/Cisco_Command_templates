# Prompt the user for input
interface_range = input("Enter interface range (e.g. GigabitEthernet1/0/1-4): ")
channel_group_num = input("Enter channel group number (e.g. 1): ")
auto_or_desirable = input("Enter PAgP mode (auto or desirable): ")

# Port Aggregation Protocol (PAgP) - Cisco’s proprietary
# auto if a PAgp is detected
# desirable unconditionally

# Enable PAgP on the following interface
print(f"""
en
config t
interface range {interface_range}
shutdown
channel-protocol pagp
channel-group {channel_group_num} mode {auto_or_desirable}
no shutdown
""")

# Enable trunking on PAgP channel group
print(f"""
#[enable trunking on PAgP channel Group]
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
