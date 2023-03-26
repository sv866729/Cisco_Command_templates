##first create linklocal address(FE80 to FEBF range)
#use linklocal address as deafult gate way for host devices
#example of link local address fe80::1
#ipv6 address example: 2001:db8:aaaa:1::/64 

#if you create a ipv6 address the linklocal will autoconfigure



# Manual configuration of IPv6 addresses with link-local address
interface = input("Enter interface name: ")
global_ipv6_address = input("Enter global IPv6 address (with prefix length): ")
link_local_address = input("Enter link-local IPv6 address: ")

print(f"""
en
config t
ipv6 unicast-routing
interface {interface}
ipv6 address {global_ipv6_address} eui-64
ipv6 address {link_local_address} link-local
no shutdown
exit
""")

#first create linklocal address(FE80 to FEBF range)
#use linklocal address as deafult gate way for host devices
#example of link local address fe80::1
#ipv6 enable creats link local address
# auto config creats the eui-64 address or global address this 
#is the == to ipv4 address

# Automatic configuration of IPv6 addresses with link-local and global unicast addresses
interface = input("Enter interface name: ")

print(f"""
en
config t
ipv6 unicast-routing
interface {interface}
ipv6 enable
ipv6 address autoconfig
no shutdown
exit
""")


