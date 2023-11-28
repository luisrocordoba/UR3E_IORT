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
conn = odbc.connect(connection_string)

#COMANDO SQL PARA LECTURA ANTES DE CAMBIO
sql= """
SELECT *
FROM horario
"""

#CREACIÓN DE CURSOR
cursor = conn.cursor()
cursor.execute(sql)

#CONVERSION A DATAFRAME E IMPRESIÓN CON LOS PRIMEROS VALORES
dataset = cursor.fetchall()
columns=[column[0] for column in cursor.description]
df= pd.DataFrame(dataset, columns=columns)
print(df)

#COMANDO SQL PARA ACTULIZAR VALORES
sql= """
		UPDATE horario
		SET "Dias = 'Jueves', Sueldo='500'"
		WHERE Usuario = 'user1';
"""
#CREACIÓN DE CURSOR
cursor = conn.cursor()
cursor.execute(sql)

#CONFIRMACION PARA ACTUALIZAR PERMANENTEMENTE LA BASE DE DATOS
conn.commit()

#CONVERSION A DATAFRAME Y SEGUNDA IMPRESIÓN CON VALORES ACTUALIZADOS
dataset = cursor.fetchall()
columns=[column[0] for column in cursor.description]
df= pd.DataFrame(dataset, columns=columns)
print(df)