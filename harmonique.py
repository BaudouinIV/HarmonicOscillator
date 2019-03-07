import math
from tkinter import Tk, Canvas

WIDTH = HEIGHT = 500
SIZE = 50
LENGTH = 300
GRAVITY = 9.81
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
color = 'black'

ZO = 0  # l'origine en z

# Solution de la forme z = A*cos(w0t + phi)
# a t = 0 => z = A*cos(phi) = (z0 - zo)
# a t = 0 => -A*sin(phi) = v0

phi = math.atan(-v0/(zo - z0))
A = math.sqrt((zo - z0)**2 + v0**2)

class Oscillator:
    def __init__(self, z0=0, v0=0, k=1, m=1):
        self._wall = canvas.create_line(0, HEIGHT // 5,
                                        WIDTH, HEIGHT // 5)
        self._string = canvas.create_line(WIDTH // 2, HEIGHT // 5,
                                          WIDTH // 2, ZO + z0)
        
        # Initial position and velocity
        self.z0 = z0
        self.v0 = v0

        # Physical constants
        self.k = k
        self.m = m
        self.w0 = math.sqrt(k/m)
        self.amplitude = 0
        self.phase = 0

        # Computing part
        self.tick = 0  # Equivalent of time
        self.__resolve_initial()
        self.__move_active()

    def __resolve_initial(self):
        self.phase = math.atan(-self.v0/(self.z0 - ZO))
        self.amplitude = math.sqrt((ZO - z0)**2 + v0**2)
        
    def __update(self):
        x = LENGTH * sin(self.theta)
        y = LENGTH * cos(self.theta)
        x_off = WIDTH // 2
        y_off = 0
        canvas.coords(self._ball,
                      x - SIZE // 2 + x_off,
                      y - SIZE // 2 + y_off,
                      x + SIZE // 2 + x_off,
                      y + SIZE // 2 + y_off)
        canvas.coords(self._string, x_off, y_off, x + x_off, y + y_off)
        self.theta = self.amplitude * cos(sqrt(LENGTH / GRAVITY)*self.tick
                                          + self.phaseo)

    def __move_active(self):
        self.__update()
        self.tick += 1/50
        tk.after(50, self.__move_active)


pendulum = Pendulum(theta=pi/4)
tk.mainloop()



