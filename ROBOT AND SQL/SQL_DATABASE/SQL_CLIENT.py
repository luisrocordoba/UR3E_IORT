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

#CREACIÓN DE CURSOR
conn = odbc.connect(connection_string)
cursor = conn.cursor()

while True:
	#OPCIONES DEL MENU
	print("Hola! Selecciona una opción:")
	print("Opción 1: Suma de dos numero\nOpción 2: Resta de dos números\nOpción 3: Salir")
	
	option=input("Opción: ")
	
    #DESICIÓN DE ACCION
    #SUMA
	if option=="1":
		a=input("Ingresa el primer número: ")
		b=input("Ingresa el segundo número: ")
		sql= f"""
			UPDATE menu
			SET elementoa = '{a}', elementob='{b}', opcion='1', estado='1'
			WHERE estado = '0';
		"""
		cursor.execute(sql)
		conn.commit()
		while True:
			sql= """
				SELECT *
				FROM menu
			"""
			cursor.execute(sql)
			dataset = cursor.fetchall()
			columns=[column[0] for column in cursor.description]
			df= pd.DataFrame(dataset, columns=columns)
			state=df["estado"][0]
			if state=="0":
				break
		print("El resultado es: ",df["resultado"][0], "\n")
	
    #RESTA
	elif option=="2":
		a=input("Ingresa el primer número: ")
		b=input("Ingresa el segundo número: ")
		sql= f"""
			UPDATE menu
			SET elementoa = '{a}', elementob='{b}', opcion='2', estado='1'
			WHERE estado = '0';
		"""
		cursor.execute(sql)
		conn.commit()
		while True:
			sql= """
				SELECT *
				FROM menu
			"""
			cursor.execute(sql)
			dataset = cursor.fetchall()
			columns=[column[0] for column in cursor.description]
			df= pd.DataFrame(dataset, columns=columns)
			state=df["estado"][0]
			if state=="0":
				break
		print("El resultado es: ", df["resultado"][0], "\n")
	#SALIR DEL PROGRAMA
	elif option=="3":
		print("Gracias por usar el programa")
		break
	
    #OPCION NO VALIDA
	else:
		print("Opción no valida, intenta de nuevo\n")