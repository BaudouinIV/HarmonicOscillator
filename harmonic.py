import math
from tkinter import Tk, Canvas

# Physical constants in SI
GRAVITY = 9.81
RHO = 2200  # Béton
MASS_DIM = {"width": 0.1, "height": 0.1, "depth": 0.1}  # A block typically
L0 = 0.3  # Longueur à l'origine du fil : 30cm
K = 20  # Stiffness
ZO = 0  # L'origine en z

# Computer part and macros
M_T_P = lambda x: x*100  # Conversion : 10 cm = 100px
get_vol = lambda x: x["width"]*x["height"]*x["depth"]

# Draw part
WIDTH = HEIGHT = 500
tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="grey")
canvas.pack()
color = 'black'

# Solution de la forme z = A*cos(w0t + phi)
# a t = 0 => z = A*cos(phi) = (z0 - zo)
# a t = 0 => -A*sin(phi) = v0
#
# phi = math.atan(-v0/(zo - z0))
# A = math.sqrt((zo - z0)**2 + v0**2)

class Oscillator:
    def __init__(self, options={}):
        self.t = 0
        self.rho = options.get("rho", RHO)
        self.dim = options.get("mass_dim", MASS_DIM)
        self.rest_length = options.get("l0", L0)
        self.stiffness = options.get("k", K)
        self.x = options.get("x", 0.1)
        self.A = self.x  # Supposing no velocity
        self.total_mass = self.rho * get_vol(self.dim)
        self.full_length = self.total_mass * GRAVITY / self.stiffness
        self.w0 = math.sqrt(self.stiffness / self.total_mass)


        # Graphisms
        self._wall = canvas.create_line(0, HEIGHT // 5,
                                          WIDTH, HEIGHT // 5)
        self._string = canvas.create_line(WIDTH // 2, HEIGHT // 5,
                                          WIDTH // 2, HEIGHT // 5 + M_T_P(self.full_length) + M_T_P(self.x))
        self._mass = canvas.create_rectangle(WIDTH // 2 - M_T_P(self.dim["width"]) // 2, HEIGHT // 5 + M_T_P(self.full_length) + M_T_P(self.x),
                                             WIDTH // 2 + M_T_P(self.dim["width"]) // 2, HEIGHT // 5 + M_T_P(self.full_length) + M_T_P(self.x) + M_T_P(self.dim["height"]))
        self.__move_active()

    def __update(self):
        self.x = self.A * math.cos(self.w0 * self.t)

    def __draw(self):
        canvas.coords(self._string, WIDTH // 2, HEIGHT // 5,
                                    WIDTH // 2, HEIGHT // 5 + M_T_P(self.full_length) + M_T_P(self.x))
        canvas.coords(self._mass, WIDTH // 2 - M_T_P(self.dim["width"]) // 2, HEIGHT // 5 + M_T_P(self.full_length) + M_T_P(self.x),
                                   WIDTH // 2 + M_T_P(self.dim["width"]) // 2, HEIGHT // 5 + M_T_P(self.full_length) + M_T_P(self.x) + M_T_P(self.dim["height"]))

    def __move_active(self):
        self.__update()
        self.__draw()
        self.t += 1/100
        tk.after(10, self.__move_active)


osc = Oscillator(options={"x": 0.3, "k": 50, })
tk.mainloop()
