#there are to version v1 and v2
#v1 doesnt support vlsm uses broadcast for updates

#v2 
#supports vlsm
##uses multicast address of 224.0.0.9 to send routing updates
#provides clear text md5 encrytption to authenticate th source

#sends entrire routing table every 30 second high bandwidth

#RIP metric is hopcount max 15 anything over is unreachable
#RIP uses 180 second hold down timer if router doesnt recivev 
#update froma dnother router in time it makes routes serverd 

print(f"""[RIPv1]
en
config t
router rip
network {networkId}
""")
print(f"""[RIPv2]
en
config t
router rip
verison 2
no-autosummary
network {networkId}""")


#setting passive interface
#on interface not connected to a router such as a switch
#this allows updates but wont send updates via that interface
print(f"router rip \n passive-interface {passinterface}")