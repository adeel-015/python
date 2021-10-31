import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="adeel2020", database="EDUCATION")
democursor=demodb.cursor()
democursor.execute("CREATE TABLE STUDENT (admn_no int primary key, sname varchar(30), gender char(1), DOB date, stream varchar(15), marks float(4,2))")
