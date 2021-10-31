import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="adeel2020", database="EDUCATION") 
democursor=demodb.cursor()
democursor.execute("delete from student where admn_no=1356")
demodb.commit()
