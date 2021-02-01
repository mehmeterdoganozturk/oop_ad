#from ldap3 import Server, Connection, ALL

#conn = Connection('SERVER2019-VM.server.local', auto_bind=True)
#1print(conn)

#server = Server('SERVER2019-VM.server.local',  get_info=ALL)
#conn = Connection(server, auto_bind=True)
#print(server.info)
#print(server.schema)

#from ldap3 import Server, Connection, ALL, NTLM
#server = Server('SERVER2019-VM.server.local', use_ssl=True, get_info=ALL)
#conn = Connection(server, user="SERVER\\python", password="Root123", authentication=NTLM)
#print(conn)

#conn = Connection(server, 'CN=Python,CN=Users,DC=server,DC=local', 'Root123', auto_bind=True)
#print(conn)

from ldap3 import Server, Connection, ALL
server = Server('SERVER2019-VM.server.local', get_info=ALL)
conn = Connection(server, 'CN=Python,CN=Users,DC=server,DC=local', 'Root123', auto_bind=True)
conn.search('DC=server,DC=local', '(objectclass=person)')
print(conn.entries)

#*******************************************************************************
#pyad.set_defaults(ldap_server = "SERVER2019-VM.server.local", username = "python", password = "Root123")
#user = pyad.aduser.ADUser.from_cn("Users")
#print(user)
