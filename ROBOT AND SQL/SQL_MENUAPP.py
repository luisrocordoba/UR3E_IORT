import pypyodbc as odbc 
import pandas as pd 
import func_gripper
import time
import urx
from func_pp import pickplace

username = 'luis'
password = 'Superman04'

server =  'sqldatabaseur3.database.windows.net'
database = 'Pruebadb'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password
conn = odbc.connect(connection_string)
cursor = conn.cursor()

rob = urx.Robot("192.168.1.102")
rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(0, 0, 0))

sql= """
	SELECT *
	FROM tblur3
"""
cursor.execute(sql)
dataset = cursor.fetchall()
columns=[column[0] for column in cursor.description]
df= pd.DataFrame(dataset, columns=columns)
valor = int(df.iloc[-1]['id'])

while True:

	sql= """
		SELECT *
		FROM tblur3
	"""
	
	cursor.execute(sql)

	dataset = cursor.fetchall()
	columns=[column[0] for column in cursor.description]
	df= pd.DataFrame(dataset, columns=columns)
	
	newvalor=int(df.iloc[-1]['id'])
	if newvalor>valor:
		valor=newvalor
		operacion=df.iloc[-1]['operacion'].upper()
		if operacion=="COORDENADAS":
			try:
				x,y,z,rx,ry,rz=rob.getl()
				print(x,y,z,rx,ry,rz)
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='INACTIVO' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
			except:
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='INACTIVO' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()

		elif operacion=="MOVEX":
			try:
				sql= f"""
				    UPDATE tblur3
				    SET ESTADO='ACTIVO'
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
				pose=rob.getl()
				pose[0]+=0.05
				rob.movel(pose,0.05,0.05,wait=False)
				time.sleep(10)
				x,y,z,rx,ry,rz=rob.getl()
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='INACTIVO' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
			except:
				pass
		elif operacion=="ACTIVARG":
			try:
				sql= f"""
				    UPDATE tblur3
				    SET ESTADO='ACTIVO'
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
				func_gripper.activate_gripper()
				time.sleep(10)
				x,y,z,rx,ry,rz=rob.getl()
				sql= f"""
				    UPDATE tblur3
					SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='INACTIVO' 
					WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
			except:
				pass

		elif operacion=="PP":
			try:
				sql= f"""
				    UPDATE tblur3
				    SET ESTADO='ACTIVO'
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
				pickplace(rob)
				x,y,z,rx,ry,rz=rob.getl()
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='INACTIVO' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
			except:
				pass
	else: 
		pass