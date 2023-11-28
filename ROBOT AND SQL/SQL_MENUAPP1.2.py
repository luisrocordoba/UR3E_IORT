import pypyodbc as odbc 
import pandas as pd 
import func_gripper
import time
import func_rob
import math
from func_pp import pickplace,espera

username = 'luis'
password = 'Superman04'

server =  'sqldatabaseur3.database.windows.net'
database = 'Pruebadb'
connection_string = 'DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';Pwd='+password
conn = odbc.connect(connection_string)
cursor = conn.cursor()



sql= """
	SELECT *
	FROM tblur3
"""
cursor.execute(sql)
dataset = cursor.fetchall()
columns=[column[0] for column in cursor.description]
df= pd.DataFrame(dataset, columns=columns)
valor = int(df.iloc[-1]['id'])

print("Servidor Funcional")
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
	x=df.iloc[-1]['x']
	y=df.iloc[-1]['y']
	z=df.iloc[-1]['z']
	rx=df.iloc[-1]['rx']
	ry=df.iloc[-1]['ry']
	rz=df.iloc[-1]['rz']
	if newvalor>valor:
		valor=newvalor
		operacion=df.iloc[-1]['operacion'].upper()
		if operacion=="COORDENADAS":
			try:
				rob=func_rob.createrob()
				x,y,z,rx,ry,rz=rob.getl()
				print(x,y,z,rx,ry,rz)
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='INACTIVO' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
				rob.close()
			except Exception as e:
				print(e)
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='CONEXIÓN ERRONEA' 
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
				rob=func_rob.createrob()
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
				rob.close()
			except:
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='CONEXIÓN ERRONEA' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
		elif operacion=="ACTIVARG":
			try:
				sql= f"""
				    UPDATE tblur3
				    SET ESTADO='ACTIVO'
				    WHERE id = '{newvalor}';
			    """
				rob=func_rob.createrob()
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
				rob.close()
			except:
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='CONEXIÓN ERRONEA' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()

		elif operacion=="PP":
			try:
				sql= f"""
				    UPDATE tblur3
				    SET ESTADO='ACTIVO'
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
				rob=func_rob.createrob()
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
				sql= f"""
				    UPDATE tblur3
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='CONEXIÓN ERRONEA' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
		elif operacion=="HOME":
			try:
				sql= f"""
				    UPDATE tblur3
				    SET ESTADO='ACTIVO'
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
				rob=func_rob.createrob()
				home_joints=[math.radians(0),math.radians(-90),math.radians(-90),math.radians(-90),math.radians(90),0]
				a=0.3 #aceleración para movimiento
				v=0.4  #velocidad para movimiento
				rob.movej(home_joints,acc=a,vel=v,wait=False)
				espera(rob)
				x,y,z,rx,ry,rz=rob.getl()
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
				    SET X='{x}', Y='{y}', Z='{z}', RX='{rx}', RY='{ry}', RZ='{rz}', ESTADO='CONEXIÓN ERRONEA' 
				    WHERE id = '{newvalor}';
			    """
				cursor.execute(sql)
				conn.commit()
	else: 
		pass