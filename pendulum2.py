import math
import tkinter as tk
import time

okno = tk.Canvas(height=600,width=800)
okno.pack()
okno.create_line(400,0,400,600,fill='grey')
def update():
    okno.update()
    okno.update_idletasks()
    
def X(x):
    return 400+40*x

def Y(y):
    return 40*y

class Pendulum():
    def __init__(self,angle,lenght):
        self.angle = angle
        self.lenght = lenght
        self.x = 0
        self.y = 0
    
    def create(self,z,w,posonutix,posonutiy,delka):
        self.x = X(delka * math.sin(self.angle))
        self.y = abs(Y(delka * math.cos(self.angle)))
        x = self.x
        y = self.y
        okno.create_line(x+posonutix,y+posonutiy,z,w,tags='pendulum')
        okno.create_oval(x+posonutix+4,y+posonutiy+4,x+posonutix-4,y+posonutiy-4,fill='black',tags='pendulum')
u = 0
v = 0
g = 9.81
l = 1
L = 1
M = 1
m = 1

def euler_u(u,v,angle1,angle2):
    u = u + 0.01*((-g*(2*M + m)*math.sin(angle1) - m*g*math.sin(angle1 - 2*angle2) - 2*math.sin(angle1-angle2)*m*(l*(v**2)+L*(u**2)*math.cos(angle1-angle2)))/(L*(2*M+m-m*math.cos(2*angle1-2*angle2))))
    return u

def euler_v(v,u,angle1,angle2):
    v = v + 0.01*((2*math.sin(angle1-angle2)*(L*(u**2)*(M+m) + g*(M+m)*math.cos(angle1)+l*(v**2)*m*math.cos(angle1-angle2)))/(l*(2*M+m-m*math.cos(2*angle1-2*angle2))))
    return v  
            
def angle_change(angle,u):
    angle = angle + 0.01*u
    return angle
        
        
        


angle1 = 30*math.pi/180 #float(input("initial angle1? "))*math.pi/180
angle2 = 20*math.pi/180 #float(input("initial angle2? "))*math.pi/180

pendulum1 = Pendulum(angle1,L)
pendulum1.create(400,1,0,0,7)
pendulum2 = Pendulum(angle2,l)
pendulum2.create(pendulum1.x,pendulum1.y,pendulum1.x-400,pendulum1.y,4)
t = 0
while t < 600:
    u = euler_u(u,v,pendulum1.angle,pendulum2.angle)
    v = euler_v(v,u,pendulum1.angle,pendulum2.angle)
    
    
    pendulum1.angle = angle_change(pendulum1.angle,u)
    pendulum2.angle = angle_change(pendulum2.angle,v)
    
    okno.delete("pendulum")
    pendulum1.create(400,1,0,0,7)
    pendulum2.create(pendulum1.x,pendulum1.y,pendulum1.x-400,pendulum1.y,7)
    okno.create_text(34,40,text="t = "+"%.2f" % t,tags="pendulum")
    
    okno.update()
    time.sleep(0.01)   
    #if 10 < t < 10.01:
        #break
    t += 0.01
    





okno.mainloop()