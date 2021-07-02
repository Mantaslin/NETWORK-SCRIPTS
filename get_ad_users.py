#!/u-- 
from ldap3 import Server, Connection, ALL, NTLM

server = Server('172.16.140.1', get_info=ALL)
conn = Connection(server, user="ryto\\storm", password="k0mpuVAda$", authentication=NTLM)

print(conn)
ldap://172.16.140.1:389 - **cleartext** - user: CN=Storm,OU=Ryto admins,DC=Ryto,DC=lt - bound - open - <local: 192.168.121.131:50164 - remote: 172.16.140.1:**389**> - **tls not started** - listening - SyncStrategy - internal decoder'
