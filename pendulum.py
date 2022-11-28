import math
import tkinter as tk
import time
#y'' + g/l *sin y = 0
okno = tk.Canvas(height=600,width=800)

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
        self.u = 0
    
    def create(self,z,w):
        x = X(8 * math.sin(self.angle))
        y = abs(Y(8 * math.cos(self.angle)))
        okno.create_line(x,y,z,w,tags='pendulum')
        okno.create_oval(x+4,y+4,x-4,y-4,fill='black',tags='pendulum')
        
    def euler_u(self,u,b):
        u = u + 0.01*(-b*u+(-g/l)*math.sin(self.angle))
        return u
        
    def angle_change(self,u):
        self.angle = self.angle + 0.01*u
        
        
        
g = 9.81
l = 1
m = 1
okno.create_text(45,10,text='lenght = '+str(l)+"m")
f = 0
if f == 0:
    okno.create_text(40,25,text='undamped')
elif f > 0:
    okno.create_text(30,25,text='damped')
elif f < 0:
    okno.create_text(30,25,text='boosted')

angle = 60*math.pi/180#float(input("initial angle? "))*math.pi/180


pendulum = Pendulum(angle,l)
pendulum.create(400,1)
u = 0
t = 0
okno.pack()
while t < 60:
    u = pendulum.euler_u(u,f)
    pendulum.angle_change(u)
    #print(pendulum.angle)
    okno.delete('pendulum')
    pendulum.create(400,1)
    okno.create_text(34,40,text="t = "+"%.2f" % (t),tags="pendulum")
    okno.create_text(45,55,text="angle = "+"%.2f" % (pendulum.angle*180/math.pi),tags="pendulum")
    okno.update()
    time.sleep(0.01)   
    #if pendulum.angle < 0.01:
        #break
    #if 10 < t < 10.01:
        #break
    t += 0.001
    





okno.mainloop()