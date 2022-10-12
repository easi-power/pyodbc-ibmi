import pyodbc
import conf as conf


connString = "DRIVER={IBM i Access ODBC driver};DATABASE="+conf.database+";SYSTEM="+conf.hostname+";PORT="+conf.port+";PROTOCOL=TCPIP;UID="+conf.username+";PWD="+conf.password
#print(connString)

conn=pyodbc.connect(connString)
cursor = conn.cursor()
cursor.execute("select * from toolshop_dev.users")
print(cursor.fetchone())