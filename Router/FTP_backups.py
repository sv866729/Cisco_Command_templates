# Copy to TFTP server
tftp_ip_address = input("Please enter the TFTP server IP address: ")
filename = input("Please enter the filename: ")
print(f"""
en 
copy running-config tftp
{tftp_ip_address}
{filename}
""")

# Save to FTP server
ftp_username = input("Please enter the FTP username: ")
ftp_password = input("Please enter the FTP password: ")
print(f"""
en
config t
ip ftp username {ftp_username}
ip ftp password {ftp_password}
exit
""")

ftp_ip_address = input("Please enter the FTP server IP address: ")
filename = input("Please enter the filename: ")
print(f"""
en
copy running-config ftp
{ftp_ip_address}
{filename}
""")

# Copy backup from FTP server to running-config
ftp_ip_address = input("Please enter the FTP server IP address: ")
filename = input("Please enter the filename: ")
print(f"""
copy ftp:running-config
{ftp_ip_address}
{filename}
""")
