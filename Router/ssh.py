hostname = input("Please enter the hostname: ")
domain_com = input("Please enter Domain name here EX: domain.com : ")  # hard-coded value
keysizebtyes = input("Please enter the RSA key size here example 512,1024,2048: ")  # hard-coded value
username = input("Please enter the username: ")
password = input("Please enter the password: ")
ipaddress = input("Please enter the IP address: ")
subnet = input("Please enter the IP address Subnet here example 255.255.255.0 : ") 




print(f"""
en
config t
hostname {hostname}
ip domain-name {hostname}.{domain_com}
crypto key generate rsa
{keysizebtyes}
!
line vty 0 15
transport input ssh
login local
exit
username {username} password {password}
service password-encryption

interface vlan1
ip address {ipaddress} {subnet}
exit



""")

