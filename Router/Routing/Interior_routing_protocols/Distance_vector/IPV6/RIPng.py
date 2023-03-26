#RIPng [Routing Information Protocol, Next Generation] Routing
#Similar to IPv4. Distance-vector, hop limit of 15, split-horizon, multicast based (FF02::9); classful
#No network statements - added to each interface individually; 
#identified by a locally significant process name  [tag]

print(f"""
#setting up RIP
en
config t
ipv6 unicast-routing
ipv6 router rip {tag}

#configuring interface
#set this up on every interface with RiP enabled
interface {ipv6interface}
ipv6 address{ipv6address}/64
ipv6 rip t{tag} enable
no shutdown
""")