#distance Vector and linkstate routning 
#the network is refering to the network that your routing say the internal network is 10.0.0.0/24 you want to put 10.0.0.0 in that spot
#not autosum keeps it classless example class a b c and say you have a 10.0.0.0/24 
#shares information only with neigboring routers

print(f"""
en
config t
router eigrp {autonomous_system_number}
network {networks_your_sharing}
network {networks_your_sharing2}
network {networks_your_sharing3}
#i dont see this command on packettracer (below)
no auto-summary

bandwidth {kb_amount_of_bandwidth_EIGRP_can_Use}
""")
###
#show ip route
#show running-configuration
#show ip protocols
#show ip eigrp neighbors
###

#setting passive interface
#on interface not connected to a router such as a switch
#this allows updates but wont send updates via that interface
print(f"router eigrp \n passive-interface {passinterface}")