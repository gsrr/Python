import sys
import MySQLdb
import lib


def connectSQL(paras):
    connection = MySQLdb.connect(paras['host'], paras['user'], paras['passwd'])
    cursor = connection.cursor()
    return connection, cursor

    
def showDB(paras):
    connection, cursor = connectSQL(paras)
    sql = "SHOW DATABASES;"
    cursor.execute(sql)
    response = cursor.fetchall()
    connection.close()
    print response
    

def createDB(paras):
    pass

def connectDB(func):
    def warp_func(paras):
        print "warp"
        connection = MySQLdb.connect(host='127.0.0.1', user=paras['user'], passwd=paras['password'], db=paras['db'])
        cursor = connection.cursor()
        paras['cursor'] = cursor
        return func(paras)
        connection.close()
    return warp_func
    
def showTable(paras):
    cursor = paras['cursor']
    sql = "SHOW TABLES;"
    cursor.execute(sql)
    response = cursor.fetchall()
    print response

def createTable(paras):
    cursor = paras['cursor']
    sql = """CREATE TABLE %s (
         ID  CHAR(20) NOT NULL,
         LABEL  CHAR(32),
         PATH  CHAR(255)
         )"""%(paras['table'])

    cursor.execute(sql)

    
def showItems(paras):
    cursor = paras['cursor']
    sql = "SELECT * FROM %s;"%paras['table']
    cursor.execute(sql)
    response = cursor.fetchall()
    return response

def insertElement(paras):
    cursor = paras['cursor']
    sql = "INSERT INTO %s VALUES ('%s', '%s', '%s');"%(paras['table'], paras['id'], paras['label'], paras['path'])
    cursor.execute(sql)

def dropTable(paras):
    cursor = paras['cursor']
    sql = "DROP TABLE %s"%(paras['table'])
    cursor.execute(sql)
    print "Delete Table Complete"
    
@connectDB
def main(paras):
    func = getattr(sys.modules[__name__], paras["op"])
    return func(paras)
    
if __name__ == "__main__":
    paras = lib.readParas()
    main(paras)
    

