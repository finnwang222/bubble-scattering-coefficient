import numpy
import math
from math import sin
from math import pi
from math import cos
from math import asin
from math import degrees

ni = 1.33  # water refractive index
nt = 1.002  # air refractive index
r = 3e-3  # sphere radius [m]
alpha = 0.3  # void fraction

# Critical angle
theta_c = int(degrees(asin(nt / ni * sin(pi / 2))))

# For the angle which incident radiation is normal to the surface of the particle (\theta = 0)
rho_0 = pow((nt - ni) / (nt + ni), 2)
rho = 0
sigma = 0

for i in range(1, theta_c + 1):
    theta = pi * i / 180
    delta_theta = pi / 180
    phi = asin(sin(theta) * ni / nt)
    rho_i = sin(theta - phi) ** 2 / (2 * sin(theta + phi) ** 2) * (1 + cos(theta + phi) ** 2 / cos(theta - phi) ** 2)
    rho = rho + rho_0 / pi * cos(0) * sin(0) * delta_theta + 2 * rho_i * cos(theta) * sin(theta) * delta_theta

sigma = sigma + rho * pi * r ** 2 * alpha / (3 / 4 * pi * pow(r, 3))
print(rho)
print(sigma)  # unit = [1 / m]
