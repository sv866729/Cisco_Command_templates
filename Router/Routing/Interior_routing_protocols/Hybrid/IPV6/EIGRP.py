print(f"""
en
config t
ipv6 unicast-routing
ipv6 router eigrp {autonomous_system_number}
eigrp router-id {ip_format_recommend_using_ip_address}
no shutdown
exit
interface {interface}
ipv6 address {ipv6address_and_NetworkSlash}
ipv6 eigrp {autonomous_system_number}
exit

""")
