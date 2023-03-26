#Extended IP Access Lists are Very Granular, meaning the ability to be specific
#Filters packets based on
#Source and destination address
#Specific IP protocol and port number
#Range is 100 through 199

#syntax
# access-list {number} {permit / deny} {protocol} {source_address source_wildcard}  {destination_address destination_wildcard}  {port number}

#there are alot more options on the protocol ip_icmp_tcp_udp_ect.


access_list_number = input("Enter access list number (100-199): ")
permit_deny = input("Enter permit or deny: ")
protocol = input("Enter protocol (ip, tcp, udp, etc.): ")
source_address = input("Enter source address (X.X.X.X): ")
source_wildcard = input("Enter source wildcard mask (X.X.X.X): ")
destination_address = input("Enter destination address (X.X.X.X): ")
destination_wildcard = input("Enter destination wildcard mask (X.X.X.X): ")
port_number = input("Enter port number (if applicable): ")
in_out = input("Enter direction (in or out): ")
interface = input("Enter interface to apply access list to: ")


print(f"""access-list {access_list_number} {permit_deny} {protocol} {source_address} {source_wildcard} {destination_address} {destination_wildcard} eq {port_number}""")


print(f"""
#[set to interface]
interface {interface}
ip access-group {access_list_number} {in_out}""")

print(f"""
Show access-list 

Show ip access-list 

Show ip interface 

Show running-configuration  """) 

   # There are so many variables you can no do this as a template efficently

#[THESE ARE SOME EXAMPLES,  THERE ARE MANY OTHER WAYS]

   # Allow all IP traffic from a specific subnet to a specific host on any port
        #access-list 101 permit ip 192.168.1.0 0.0.0.255 host 10.0.0.5


    #Deny all TCP traffic from a specific host to a specific subnet on port 22
        #access-list 102 deny tcp host 10.0.0.5 eq 22 192.168.1.0 0.0.0.255


    #Permit all UDP traffic between two specific subnets
        #access-list 103 permit udp 172.16.0.0 0.0.255.255 192.168.0.0 0.0.255.255


    #Deny all traffic from a specific host to any destination
         #access-list 104 deny ip host 192.168.1.10 any


    #Permit all ICMP traffic between two specific hosts
        #access-list 105 permit icmp host 10.0.0.5 host 10.0.0.10


    #Deny all traffic except HTTP and HTTPS from a specific subnet to any destination
        #access-list 106 deny ip 192.168.1.0 0.0.0.255 any
        #access-list 106 permit tcp 192.168.1.0 0.0.0.255 any eq 80
        #access-list 106 permit tcp 192.168.1.0 0.0.0.255 any eq 443


    #Permit all TCP traffic to a specific host on any port
        #access-list 107 permit tcp any host 10.0.0.5


    #Deny all traffic from a specific subnet to any destination on ports 20-21
        #access-list 108 deny tcp 192.168.1.0 0.0.0.255 any range 20 21


    #Permit all traffic from a specific host to a specific subnet on any port
        #access-list 109 permit ip host 10.0.0.5 192.168.1.0 0.0.0.255


    #Deny all traffic to a specific host on any port
        #access-list 110 deny ip any host 10.0.0.5

