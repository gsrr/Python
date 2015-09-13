import sys
import MySQLdb
import lib
import copy
import json


def connectSQL(paras):
    connection = MySQLdb.connect(paras['host'], paras['user'], paras['passwd'])
    cursor = connection.cursor()
    return connection, cursor

    
def showDB(paras):
    cursor = paras['cursor']
    sql = "SHOW DATABASES;"
    cursor.execute(sql)
    response = cursor.fetchall()
    ret = []
    for item in response:
        ret.append(item[0])
    print ret
    return ret
    

def createDB(paras):
    pass

def connectDB(func):
    def warp_func(paras):
        connection = None
        if paras['op'] == "showDB":
            connection = MySQLdb.connect(host='127.0.0.1', user=paras['user'], passwd=paras['password'])
        else:
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
    ret = []
    for item in response:
        ret.append(item[0])
    print ret
    return ret

def createTable(paras):
    cursor = paras['cursor']
    sql = """CREATE TABLE %s (
         ID  CHAR(20) NOT NULL,
         LABEL  CHAR(32),
         PATH  CHAR(255)
         )"""%(paras['table'])

    cursor.execute(sql)

def sqlCondition(condStr):
    ret = ""
    strArr = condStr.split()
    for i in range(0, len(strArr), 2):
        item = "Label LIKE '%%%s%%' "%(strArr[i])
        ret += item
        if i+1 < len(strArr):
            ret += (strArr[i+1] + " ")
    return ret
def showItems(paras):
    cursor = paras['cursor']
    
    if paras.has_key("condition") and paras["condition"] != "":
        sql = "SELECT * FROM %s WHERE %s;"%(paras['table'], sqlCondition(paras['condition']))
    else:
        sql = "SELECT * FROM %s;"%(paras['table'])
    cursor.execute(sql)
    response = cursor.fetchall()
    ret = []
    for item in response:
        data = [item[0], item[1] , item[2]]
        ret.append(copy.deepcopy(data))
    print json.dumps(ret)
    return ret

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
    

