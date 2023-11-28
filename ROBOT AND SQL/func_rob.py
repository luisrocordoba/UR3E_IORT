import urx
import time
a=0.05 #aceleración para movimiento
v=0.05  #velocidad para movimiento

def espera(rob):
	while 1:
		pose=rob.getl()
		pose_r=[round(x, 3) for x in pose]
		time.sleep(1)
		pose_2=rob.getl()
		pose_r2=[round(x, 3) for x in pose_2]
		if all(x == y for x, y in zip(pose_r, pose_r2)):
			break
            
def createrob():
    rob = urx.Robot("192.168.1.102")
    rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
    rob.set_payload(1.040,(0, 0, 0))
    return rob

def movex(rob,x):
    pose=rob.getl()
    pose[0]+=(x/100)
    rob.movel(pose,acc=a,vel=v,wait=False)
    espera(rob)

def movey(rob,y):
    pose=rob.getl()
    pose[1]+=(y/100)
    rob.movel(pose,acc=a,vel=v,wait=False)
    espera(rob)

def movez(rob,z):
    pose=rob.getl()
    pose[2]+=(z/100)
    rob.movel(pose,acc=a,vel=v,wait=False)
    espera(rob)

def movepunto(rob,x,y,z):
    pose=rob.getl()
    pose[0]=(x/100)
    pose[1]=(y/100)
    pose[2]=(z/100)
    rob.movel(pose,acc=0.009,vel=0.009,wait=False)
    espera(rob)