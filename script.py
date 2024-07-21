import MySQLdb as mdb

# Example usage
connection = mdb.connect(host="localhost", user="user", passwd="passwd", db="dbname")
cursor = connection.cursor()
cursor.execute("SELECT VERSION()")
version = cursor.fetchone()
print(f"MySQL version: {version[0]}")
connection.close()
