# Prompt user for input for inside interface
insideint = input("Enter inside interface (e.g. Ethernet1/1): ")
insideip = input("Enter inside IP address (e.g. 192.168.1.1): ")
insidesub = input("Enter inside subnet mask (e.g. 255.255.255.0): ")

# Prompt user for input for guest interface
guestint = input("Enter guest interface (e.g. Ethernet1/2): ")
guestip = input("Enter guest IP address (e.g. 192.168.2.1): ")
guestsub = input("Enter guest subnet mask (e.g. 255.255.255.0): ")

# Prompt user for input for outside interface
outsideint = input("Enter outside interface (e.g. Ethernet1/3): ")
outsideid = input("Enter outside IP address (e.g. 203.0.113.1): ")
outsidesub = input("Enter outside subnet mask (e.g. 255.255.255.0): ")

# Use variables in the configuration template
print(f"""
Interface {insideint}
Nameif inside
	Ip address {insideip} {insidesub}
Security-level 100
	No shutdown
	

Interface {guestint}
Ip address  {guestip} {guestsub}
Nameif guest
Security-level 50
No shutdown

Interface {outsideint}
Nameif outside
Security-level 0
Ip address  {outsideid} {outsidesub}
Nameif outside
No shutdown
!
Ex
""")
