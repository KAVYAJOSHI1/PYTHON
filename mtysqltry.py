import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='Kavya@1512',database='try')
#print(conn)
my_cursor=conn.cursor()
#my_cursor.execute("CREATE DATABASE mydatabase")
#my_cursor.execute("SHOW DATABASES")
#for x in my_cursor:
 #   print(x)
#my_cursor.execute("SHOW TABLES")
#for x in my_cursor:
    #print(x)
#my_cursor.execute("create table next(a int,b varchar(15),c set('1','2'))")
#result=my_cursor.fetchone()
#print(result)
sql="INSERT INTO next (a,b,c) VALUES (%s,%s,%s)"
val=(1,"abc",1)
my_cursor.execute(sql,val)
conn.commit()
print(my_cursor.rowcount,"was inserted")