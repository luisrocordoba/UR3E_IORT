#LIBRERIAS A UTILIZAR
import pypyodbc as odbc 
import pandas as pd
import time

#USUARIO Y CONTRASEÑA DE LA BASE DE DATOS
username = 'luis'
password = 'Superman04'

#DIRECCIÓN DEL SERVIDOR
server =  'sqldatabaseur3.database.windows.net'
#NOMBRE DE LA BASE DE DATOS
database = 'Pruebadb'

#CADENA DE CONEXION Y CONEXION A BASE DE DATOS
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password

#CREACION DE CURSOS
conn = odbc.connect(connection_string)
cursor = conn.cursor()
while True:
	print("Hola! Selecciona una opción:")
	print("Opción 1: Mapeo\nOpción 2:Salir")
	
	option=input("Opción: ")
	if option=="1":
		sql= f"""
			UPDATE ur3
			SET estado='1', conexion='1', operacion='1' 
			WHERE estado = '0';
		"""
		cursor.execute(sql)
		conn.commit()
		time.sleep(5)
		sql= """
			SELECT *
			FROM ur3
		"""
		cursor.execute(sql)
		dataset = cursor.fetchall()
		columns=[column[0] for column in cursor.description]
		df= pd.DataFrame(dataset, columns=columns)
		link=df['conexion'][0]
		if link=="2":
			print("Conexion lograda")
			print(f"El PCH se encuentra en\nx={df['x'][0]}\ny={df['y'][0]}\nz={df['z'][0]}\nrx={df['rx'][0]}\nry={df['ry'][0]}\nrz={df['rz'][0]}")
			sql= f"""
			UPDATE ur3
			SET conexion='0' 
			WHERE estado = '0';
			"""
			cursor.execute(sql)
			conn.commit()
		else:
			print("Conexion erronea, intenta de nuevo")
			sql= f"""
			UPDATE ur3
			SET conexion='0' 
			WHERE estado = '0';
			"""
			cursor.execute(sql)
			conn.commit()
	elif option=="2":
		print("Gracias por usar el programa")
		break
	else:
		print("Opción no valida, intenta de nuevo\n")
	