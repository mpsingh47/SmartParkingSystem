import pymysql 
#from pymysql import *

def Connect():
    conn=pymysql.connect(host="127.0.0.1",user="root",password="",database="smart_parking_system")
    return conn
