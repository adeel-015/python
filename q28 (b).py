import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="adeel2020", database="EDUCATION") 
democursor=demodb.cursor()
democursor.execute("insert into student values (%s, %s, %s, %s, %s, %s)",
(1245, 'Arush', 'M', '2003-10-04', 'science', 67.34))
demodb.commit()
