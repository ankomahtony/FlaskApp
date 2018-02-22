import MySQLdb

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user="root",
                           passwd="rep2",
                           db="tonydb")
    c = conn.cursor()

    return c, conn