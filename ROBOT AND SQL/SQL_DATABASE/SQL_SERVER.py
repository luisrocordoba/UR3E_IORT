#LIBRERIAS A UTILIZAR
import pypyodbc as odbc 
import pandas as pd
#USARIO Y CONTRASEÑA DE LA BASE DE DATOS
username = 'luis'
password = 'Superman04'

#DIRECCIÓN DEL SERVIDOR
server =  'sqldatabaseur3.database.windows.net'
#NOMBRE DE LA BASE DE DATOS
database = 'Pruebadb'

#CADENA DE CONEXION Y CONEXION A BASE DE DATOS
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password

#CICLO INFINITO
while True:
	#CREACIÓN DE CURSOR
	conn = odbc.connect(connection_string)
	cursor = conn.cursor()
	sql= """
		SELECT *
		FROM menu
	"""
	cursor.execute(sql)
	#CONVERSION A DATAFRAME
	dataset = cursor.fetchall()
	columns=[column[0] for column in cursor.description]
	df= pd.DataFrame(dataset, columns=columns)
	print(df)
	
    #LECTURA DEL ESTADO DEL SERVIDOR
	if df["estado"][0]=="1":
		
		#LECTURA DE LA OPERACIÓN A REALIZAR
		if df["opcion"][0]=="1":
			resultado=int (df["elementoa"][0]) + int(df["elementob"][0])
		elif df["opcion"][0]=="2":
			resultado=int (df["elementoa"][0]) - int(df["elementob"][0])
		
        #ACTUALIZACIÓN DE TABLA
		sql= f"""
				UPDATE menu
				SET estado='0', resultado='{resultado}'
				WHERE estado = '1';
			"""
		cursor.execute(sql)
		conn.commit()
	else: 
		pass