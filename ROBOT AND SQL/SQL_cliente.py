import pypyodbc as odbc 
import pandas as pd
import time
username = 'luis'
password = 'Superman04'
server =  'sqldatabaseur3.database.windows.net'
database = 'Pruebadb'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password
conn = odbc.connect(connection_string)
cursor = conn.cursor()
while True:
	print("Hola! Selecciona una opción:")
	print("Opción 1: Mapeo\nOpción 2: Movimiento en x\nOpción 3: Activación Gripper\nOpción 4: Salir")
	while 1:
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
			sql= f"""
				UPDATE ur3
				SET estado='1', conexion='1', operacion='2' 
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
				time.sleep(10)
				sql= """
					SELECT *
					FROM ur3
				"""
				cursor.execute(sql)
				dataset = cursor.fetchall()
				columns=[column[0] for column in cursor.description]
				df= pd.DataFrame(dataset, columns=columns)
				print(f"La nueva posición PCH se encuentra en\nx={df['x'][0]}\ny={df['y'][0]}\nz={df['z'][0]}\nrx={df['rx'][0]}\nry={df['ry'][0]}\nrz={df['rz'][0]}")
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
		elif option=="3":
			sql= f"""
				UPDATE ur3
				SET estado='1', conexion='1', operacion='3' 
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
				print("Activando Gripper")
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
		elif option=="4":
			print("Gracias por usar el programa!")
			break
		else:
			print("Opción no valida, intenta de nuevo\n")
	break