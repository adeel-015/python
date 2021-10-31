import mysql.connector
demodb = mysql.connector.connect(host="localhost", user="root", passwd="adeel2020", database="EDUCATION")
democursor=demodb.cursor()
democursor.execute("update student set marks=55.68 where admn_no=1356")
demodb.commit()
