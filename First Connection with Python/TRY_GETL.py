import urx

rob = urx.Robot("192.168.1.102")
rob.set_tcp((0, 0,  0.150, 0, 0, 0)) #Definimos la ubicación del EF montado al robot
rob.set_payload(1.040,(0, 0, 0))
pose=rob.getl()
print(pose)