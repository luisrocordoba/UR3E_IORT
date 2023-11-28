import pypyodbc as odbc 
import pandas as pd 
username = 'luis'
password = 'Superman04'

server =  'sqldatabaseur3.database.windows.net'
database = 'Pruebadb'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password
conn = odbc.connect(connection_string)


sql= """
	SELECT *
	FROM menu
"""
cursor = conn.cursor()
cursor.execute(sql)

dataset = cursor.fetchall()
columns=[column[0] for column in cursor.description]
df= pd.DataFrame(dataset, columns=columns)
print(df)