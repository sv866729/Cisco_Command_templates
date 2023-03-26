
poolname = input("DHCP pool name: ")
NetoworkIP = input("DHCP network: ")
subnet = input("DHCP Subnet: ")
dnsip = input("DNS IP: ")
defaultgateway = input("Default Gateway: ")
domainname = input("Domain Namer: ")
day = input("DHCP Lease days: ")
hours = input("DHCP lease hours: ")
minutes = input("DHCP lease seconds: ")
replayinterface = input("DHCP replay interface: ")
replayip = input ("replay agent IP address: ")
#DHCO on router device
print("en \n config t")
print("service dhcp")
#Define address pool
print(f"ip dhcp pool {poolname} \n network {NetoworkIP} {subnet}")
#client perameters
print (f"""
dns-server {dnsip}
default-router {defaultgateway}
domain-name {domainname}
lease {day} {hours} {minutes}
ex

ip dhcp excluded-address {exculded address}

""")


#replay agent set up
print(f"interface {replayinterface} \n ip helper-address {replayip} ")

#verify show commands

#show ip dhcp binding   
#show ip dhcp server statistics
#debug ip dhcp server