#steps first crearte the list then apply the list
#this will not be a template more of a reference due to the amount of options
#thing to not it that theses rules are exicuted in order with a implicit deny if a any any rule isnt stated last 
#ACL can also be a name


#creating ACL
print("""en
config t
access-list 100 deny(action) tcp any(source) any(detination) eq ftp-data
access-list 100 deny tcp any any eq ftp
access-list 100 permit ip any any
""")

#applying AC
print(f"""interface 100
ip access-group 100 out
#this th direction that the list is being applied so ftp can come in but not out of this interface) 
""")

#show access-list
#show access-list 100
