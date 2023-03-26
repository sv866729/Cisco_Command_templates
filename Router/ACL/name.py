#theses ACL follow same standards as exteded and standards
#will show how to get to the option of which to follow
standard_extended = input("Enter Standard or Extended: ")
name = input("Enter Name for the access list: ")
interface = input("Enter Interface: ")
in_out = input("Enter In or Out: ")

print(f"""ip access-list {standard_extended} {name}
#follow syntax for the extended or standard after this part""")

print(f"""
#[set to interface]
interface {interface}
ip access-group {name} {in_out}""")

print(f"""
Show access-list 

Show ip access-list 

Show ip interface 

Show running-configuration  """)