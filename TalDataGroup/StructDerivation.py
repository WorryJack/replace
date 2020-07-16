import cx_Oracle as oracle
import configparser



# cursor = oracle.connect('haxesbi' , 'IuT7FcLmQa1Z', '192.168.11.194').cursor()

table_list = ['DN_CLASS_COUNT']
for i in table_list:
    sql = "SELECT * FROM col WHERE tname = " + "'" + i + "'" +" ORDER BY tname,colno "
    print(sql)