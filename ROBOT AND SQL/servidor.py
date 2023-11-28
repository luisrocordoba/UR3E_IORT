import pypyodbc as odbc 
import pandas as pd 
username = 'luis'
password = 'Superman04'

server =  'sqldatabaseur3.database.windows.net'
database = 'Pruebadb'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password


while True:
	conn = odbc.connect(connection_string)
	cursor = conn.cursor()
	sql= """
		SELECT *
		FROM menu
	"""
	
	cursor.execute(sql)

	dataset = cursor.fetchall()
	columns=[column[0] for column in cursor.description]
	df= pd.DataFrame(dataset, columns=columns)
	print(df)
	if df["estado"][0]=="1":
		print("Si")
		if df["opcion"][0]=="1":
			resultado=int (df["elementoa"][0]) + int(df["elementob"][0])
			sql= f"""
					UPDATE menu
					SET estado='0', resultado='{resultado}'
					WHERE estado = '1';
				"""
			cursor.execute(sql)
			conn.commit()
		elif df["opcion"][0]=="2":
			resultado=int (df["elementoa"][0]) - int(df["elementob"][0])
			sql= f"""
					UPDATE menu
					SET estado='0', resultado='{resultado}'
					WHERE estado = '1';
				"""
			cursor.execute(sql)
			conn.commit()
	else: 
		pass