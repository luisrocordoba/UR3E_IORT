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



rob = urx.Robot("192.168.1.102")
rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(0, 0, 0))

while True:
	conn = odbc.connect(connection_string)
	cursor = conn.cursor()
	sql= """
		SELECT *
		FROM ur3
	"""
	
	cursor.execute(sql)

	dataset = cursor.fetchall()
	columns=[column[0] for column in cursor.description]
	df= pd.DataFrame(dataset, columns=columns)
	if df["estado"][0]=="1":
		if df["operacion"][0]=="1":
			try:
				x,y,z,rx,ry,rz=rob.getl()
				sql= f"""
					UPDATE ur3
					SET estado='0', conexion='2', x='{x}', y='{y}', z='{z}', rx='{rx}', ry='{ry}', rz='{rz}' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
			except Exception as e:
				print(e)
				sql= f"""
					UPDATE ur3
					SET estado='0', conexion='3' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
		elif df["operacion"][0]=="2":
			try:
				sql= f"""
					UPDATE ur3
					SET conexion='2'
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
				pose=rob.getl()
				pose[0]+=0.05
				rob.movel(pose,0.05,0.05,wait=False)
				time.sleep(10)
				x,y,z,rx,ry,rz=rob.getl()
				sql= f"""
					UPDATE ur3
					SET estado='0', conexion='2', x='{x}', y='{y}', z='{z}', rx='{rx}', ry='{ry}', rz='{rz}' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
			except Exception as e:
				print(e)
				sql= f"""
					UPDATE ur3
					SET estado='0', conexion='3' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
		elif df["operacion"][0]=="3":
			try:
				sql= f"""
					UPDATE ur3
					SET conexion='2'
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
				func_gripper.activate_gripper()
				sql= f"""
					UPDATE ur3
					SET estado='0' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
			except Exception as e:
				print(e)
				sql= f"""
					UPDATE ur3
					SET estado='0', conexion='3' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
		elif df["operacion"][0]=="4":
			try:
				sql= f"""
					UPDATE ur3
					SET conexion='2'
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
				pickplace(rob)
				sql= f"""
					UPDATE ur3
					SET estado='0' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
			except Exception as e:
				print(e)
				sql= f"""
					UPDATE ur3
					SET estado='0', conexion='3' 
					WHERE estado = '1';
				"""
				cursor.execute(sql)
				conn.commit()
	else: 
		pass