import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="adeel2020", database="EDUCATION") 
democursor=demodb.cursor()
democursor.execute("select * from student")
for i in democursor:
    print(i)
