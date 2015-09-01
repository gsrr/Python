import sys
import MySQLdb
import lib


def connectSQL(paras):
    connection = MySQLdb.connect(paras['host'], paras['user'], paras['passwd'])
    cursor = connection.cursor()
    return cursor

    
def showDB(paras):
    cursor = connectSQL(paras)
    sql = "SHOW DATABASES;"
    cursor.execute(sql)
    response = cursor.fetchall()
    print response

def createDB(paras):
    pass
    
def connectDB(paras):
    connection = MySQLdb.connect(host=paras['host'], user=paras['user'], passwd=paras['passwd'], db="mysql")
    cursor = connection.cursor()
    return cursor
    
def showTable(paras):
    cursor = connectDB(paras)
    sql = "SHOW TABLES;"
    cursor.execute(sql)
    response = cursor.fetchall()
    print response

def createTable(paras):
    pass
    
if __name__ == "__main__":
    paras = lib.readParas()
    print paras
    func = getattr(sys.modules[__name__], paras["op"])
    func(paras)

